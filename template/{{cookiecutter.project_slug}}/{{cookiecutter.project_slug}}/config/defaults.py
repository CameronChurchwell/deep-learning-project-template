import os
from pathlib import Path

import GPUtil
import yapecs


###############################################################################
# Metadata
###############################################################################


# Configuration name
CONFIG = '{{cookiecutter.project_slug}}'


###############################################################################
# Data parameters
###############################################################################


# Names of all datasets
DATASETS = []

# Datasets for evaluation
EVALUATION_DATASETS = DATASETS

# Cache metadata for datasets
MEMORY_CACHING = True


###############################################################################
# Directories
###############################################################################

# Root location for output (e.g. runs, data)
ROOT_DIR = Path(__file__).parent.parent.parent

# Location to save assets to be bundled with pip release
@yapecs.ComputedProperty(compute_once=True)
def ASSETS_DIR():
    import {{cookiecutter.project_slug}}
    return {{cookiecutter.project_slug}}.ROOT_DIR / '{{cookiecutter.project_slug}}' / 'assets'

# Location of preprocessed features
@yapecs.ComputedProperty(compute_once=True)
def CACHE_DIR():
    import {{cookiecutter.project_slug}}
    return {{cookiecutter.project_slug}}.ROOT_DIR / 'data' / 'cache'

# Location of datasets on disk
@yapecs.ComputedProperty(compute_once=True)
def DATA_DIR():
    import {{cookiecutter.project_slug}}
    return {{cookiecutter.project_slug}}.ROOT_DIR / 'data' / 'datasets'

# Location to save evaluation artifacts
@yapecs.ComputedProperty(compute_once=True)
def EVAL_DIR():
    import {{cookiecutter.project_slug}}
    return {{cookiecutter.project_slug}}.ROOT_DIR / 'eval'

# Location to save training and adaptation artifacts
@yapecs.ComputedProperty(compute_once=True)
def RUNS_DIR():
    import {{cookiecutter.project_slug}}
    return {{cookiecutter.project_slug}}.ROOT_DIR / 'runs'


###############################################################################
# Evaluation parameters
###############################################################################


# Number of steps between tensorboard logging
EVALUATION_INTERVAL = 2500  # steps

# Number of steps to perform for tensorboard logging
DEFAULT_EVALUATION_STEPS = 16


###############################################################################
# Training parameters
###############################################################################


# Batch size (per gpu)
BATCH_SIZE = 64

# Number of steps between saving checkpoints
CHECKPOINT_INTERVAL = 25000  # steps

# Number of training steps
STEPS = 300000

# Number of data loading worker threads
try:
    NUM_WORKERS = int(os.cpu_count() / max(1, len(GPUtil.getGPUs())))
except ValueError:
    NUM_WORKERS = os.cpu_count()

# Seed for all random number generators
RANDOM_SEED = 1234
