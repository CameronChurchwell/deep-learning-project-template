import yapecs

import {{cookiecutter.project_slug}}


###############################################################################
# Entry point
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = yapecs.ArgumentParser()
    parser.add_argument(
        '--datasets',
        default={{cookiecutter.project_slug}}.DATASETS,
        nargs='+',
        help='The names of the datasets to preprocess')
    return parser.parse_args()


{{cookiecutter.project_slug}}.data.preprocess.datasets(**vars(parse_args()))
