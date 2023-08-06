"""Anomaly Score Normalization Callback."""
from typing import Any, Dict, Optional

import pytorch_lightning as pl
import torch
from pytorch_lightning import Callback, Trainer
from pytorch_lightning.utilities.types import STEP_OUTPUT
from torch.distributions import LogNormal, Normal

from anomalib.models import get_model


class AnomalyScoreNormalizationCallback(Callback):
    """Callback that standardizes the image-level and pixel-level anomaly scores."""

    def __init__(self):
        self.image_dist: Optional[LogNormal] = None
        self.pixel_dist: Optional[LogNormal] = None

    def on_test_start(self, _trainer: pl.Trainer, pl_module: pl.LightningModule) -> None:
        """Called when the test begins."""
        pl_module.image_metrics.F1.threshold = 0.5
        pl_module.pixel_metrics.F1.threshold = 0.5

    def on_train_epoch_end(
        self, trainer: pl.Trainer, pl_module: pl.LightningModule, _unused: Optional[Any] = None
    ) -> None:
        """Called when the train epoch ends.

        Use the current model to compute the anomaly score distributions
        of the normal training data. This is needed after every epoch, because the statistics must be
        stored in the state dict of the checkpoint file.
        """
        self._collect_stats(trainer, pl_module)

    def on_validation_batch_end(
        self,
        _trainer: pl.Trainer,
        pl_module: pl.LightningModule,
        outputs: Optional[STEP_OUTPUT],
        _batch: Any,
        _batch_idx: int,
        _dataloader_idx: int,
    ) -> None:
        """Called when the validation batch ends, standardizes the predicted scores and anomaly maps."""
        self._standardize(outputs, pl_module)

    def on_test_batch_end(
        self,
        _trainer: pl.Trainer,
        pl_module: pl.LightningModule,
        outputs: Optional[STEP_OUTPUT],
        _batch: Any,
        _batch_idx: int,
        _dataloader_idx: int,
    ) -> None:
        """Called when the test batch ends, normalizes the predicted scores and anomaly maps."""
        self._standardize(outputs, pl_module)
        self._normalize(outputs, pl_module)

    def on_predict_batch_end(
        self,
        _trainer: pl.Trainer,
        pl_module: pl.LightningModule,
        outputs: Dict,
        _batch: Any,
        _batch_idx: int,
        _dataloader_idx: int,
    ) -> None:
        """Called when the predict batch ends, normalizes the predicted scores and anomaly maps."""
        self._standardize(outputs, pl_module)
        self._normalize(outputs, pl_module)
        outputs["pred_labels"] = outputs["pred_scores"] >= 0.5

    def _collect_stats(self, trainer, pl_module):
        """Collect the statistics of the normal training data.

        Create a trainer and use it to predict the anomaly maps and scores of the normal training data. Then
         estimate the distribution of anomaly scores for normal data at the image and pixel level by computing
         the mean and standard deviations. A dictionary containing the computed statistics is stored in self.stats.
        """
        predictions = Trainer(gpus=trainer.gpus).predict(
            model=self._create_inference_model(pl_module), dataloaders=trainer.datamodule.train_dataloader()
        )
        pl_module.training_distribution.reset()
        for batch in predictions:
            if "pred_scores" in batch.keys():
                pl_module.training_distribution.update(anomaly_scores=batch["pred_scores"])
            if "anomaly_maps" in batch.keys():
                pl_module.training_distribution.update(anomaly_maps=batch["anomaly_maps"])
        pl_module.training_distribution.compute()

    @staticmethod
    def _create_inference_model(pl_module):
        """Create a duplicate of the PL module that can be used to perform inference on the training set."""
        new_model = get_model(pl_module.hparams)
        new_model.load_state_dict(pl_module.state_dict())
        return new_model

    def _standardize(self, outputs: STEP_OUTPUT, pl_module) -> None:
        """Standardize the predicted scores and anomaly maps to the z-domain."""
        stats = pl_module.training_distribution.to(outputs["pred_scores"].device)

        outputs["pred_scores"] = torch.log(outputs["pred_scores"])
        outputs["pred_scores"] = (outputs["pred_scores"] - stats.image_mean) / stats.image_std
        if "anomaly_maps" in outputs.keys():
            outputs["anomaly_maps"] = (torch.log(outputs["anomaly_maps"]) - stats.pixel_mean) / stats.pixel_std
            outputs["anomaly_maps"] -= (stats.image_mean - stats.pixel_mean) / stats.pixel_std

    def _normalize(self, outputs: STEP_OUTPUT, pl_module: pl.LightningModule) -> None:
        """Normalize the predicted scores and anomaly maps by first standardizing and then computing the CDF."""
        device = outputs["pred_scores"].device
        image_threshold = pl_module.image_threshold.value.cpu()
        pixel_threshold = pl_module.pixel_threshold.value.cpu()

        norm = Normal(torch.Tensor([0]), torch.Tensor([1]))
        outputs["pred_scores"] = norm.cdf(outputs["pred_scores"].cpu() - image_threshold).to(device)
        if "anomaly_maps" in outputs.keys():
            outputs["anomaly_maps"] = norm.cdf(outputs["anomaly_maps"].cpu() - pixel_threshold).to(device)
