import yapecs

import {{cookiecutter.project_slug}}


###############################################################################
# Download datasets
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = yapecs.ArgumentParser(description='Download datasets')
    parser.add_argument(
        '--datasets',
        default={{cookiecutter.project_slug}}.DATASETS,
        nargs='+',
        help='The datasets to download')
    return parser.parse_args()


{{cookiecutter.project_slug}}.data.download.datasets(**vars(parse_args()))
