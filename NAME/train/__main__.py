import argparse
import shutil
from pathlib import Path

import NAME


###############################################################################
# Entry point
###############################################################################


def main(config, datasets, gpus=None):
    # Create output directory
    directory = NAME.RUNS_DIR / config.stem
    directory.mkdir(parents=True, exist_ok=True)

    # Save configuration
    shutil.copyfile(config, directory / config.name)

    # Train
    NAME.train.run(
        datasets,
        directory,
        directory,
        directory,
        gpus)

    # Evaluate
    NAME.evaluate.datasets(datasets, directory, gpus)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument(
        '--config',
        type=Path,
        default=NAME.DEFAULT_CONFIGURATION,
        help='The configuration file')
    parser.add_argument(
        '--datasets',
        default=NAME.DATASETS,
        nargs='+',
        help='The datasets to train on')
    parser.add_argument(
        '--gpus',
        type=int,
        nargs='+',
        help='The indices of the gpus to run training on')
    return parser.parse_args()


main(**vars(parse_args()))
