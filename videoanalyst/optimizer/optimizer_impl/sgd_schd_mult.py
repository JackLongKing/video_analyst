# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple
import numpy as np

from yacs.config import CfgNode

import torch
from torch import optim

from videoanalyst.evaluation.got_benchmark.datasets import got10k
from videoanalyst.data.dataset.dataset_base import DatasetBase
from ..optimizer_base import TRACK_OPTIMIZERS, OptimizerBase

@TRACK_OPTIMIZERS.register
class SGD_Schd_Mult(OptimizerBase):
    r"""
    Tracking data sampler

    Hyper-parameters
    ----------------
    """
    default_hyper_params = dict(
        lr=0.1,
        momentum=0.9
        weight_decay=0.00005
    )

    def __init__(self, cfg: CfgNode) -> None:
        super(SGD_Schd_Mult, self).__init__(datasets, seed=seed)

    def build_optimzier(self, model):
        kwargs = self._hyper_params
        optim.SGD(**kwargs)
    
    def schedule(self, epoch: int, iteration: int) -> None:
        