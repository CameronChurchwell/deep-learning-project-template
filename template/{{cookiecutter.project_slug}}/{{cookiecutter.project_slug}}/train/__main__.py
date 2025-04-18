import yapecs
import shutil
from pathlib import Path

import {{cookiecutter.project_slug}}


###############################################################################
# Entry point
###############################################################################


def main(config, dataset):
    """Train from configuration"""
    # Create output directory
    directory = {{cookiecutter.project_slug}}.RUNS_DIR / config.stem
    directory.mkdir(parents=True, exist_ok=True)

    # Save configuration
    shutil.copyfile(config, directory / config.name)

    # Train
    {{cookiecutter.project_slug}}.train.train(dataset, directory)


def parse_args():
    """Parse command-line arguments"""
    parser = yapecs.ArgumentParser(description='Train a model')
    parser.add_argument(
        '--config',
        type=Path,
        default={{cookiecutter.project_slug}}.DEFAULT_CONFIGURATION,
        help='The configuration file')
    parser.add_argument(
        '--datasets',
        default={{cookiecutter.project_slug}}.DATASETS,
        nargs='+',
        help='The datasets to train on')

    return parser.parse_args()


main(**vars(parse_args()))
