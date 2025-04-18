import yapecs

import {{cookiecutter.project_slug}}


def parse_args():
    """Parse command-line arguments"""
    parser = yapecs.ArgumentParser(description='Partition datasets')
    parser.add_argument(
        '--datasets',
        default={{cookiecutter.project_slug}}.DATASETS,
        nargs='+',
        help='The datasets to partition')
    return parser.parse_args()


{{cookiecutter.project_slug}}.partition.datasets(**vars(parse_args()))
