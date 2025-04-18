import json
from pathlib import Path
import torch
import torchaudio

import NAME

###############################################################################
# Download Utilities
###############################################################################

def partition(dataset):
    """Load partitions for dataset"""
    with open(NAME.PARTITION_DIR / f'{dataset}.json') as file:
        return json.load(file)

def audio(file):
    """Load audio from disk"""
    path = Path(file)
    if path.suffix.lower() == '.mp3':
        try:
            audio, sample_rate = torchaudio.load(path, format='mp3')
        except RuntimeError:
            raise RuntimeError(
                'Failed to load mp3 file, make sure ffmpeg<=4.3 is installed')
    else:
        audio, sample_rate = torchaudio.load(file)

    # Maybe resample
    return NAME.resample(audio, sample_rate)

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
