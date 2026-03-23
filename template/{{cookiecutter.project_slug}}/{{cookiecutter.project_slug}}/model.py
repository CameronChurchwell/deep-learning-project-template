import json
from pathlib import Path
import torch
{{"import torchaudio" if cookiecutter.audio == 'yes' else ""}}

import {{cookiecutter.project_slug}}

###############################################################################
# Download Utilities
###############################################################################


class Model(torch.nn.Module):
    """Model definition"""

    # TODO - add hyperparameters as input args
    def __init__(self):
        super().__init__()

        # TODO - define model
        raise NotImplementedError

    def forward(self):
        """Perform model inference"""
        # TODO - define model arguments and implement forward pass
        raise NotImplementedError
