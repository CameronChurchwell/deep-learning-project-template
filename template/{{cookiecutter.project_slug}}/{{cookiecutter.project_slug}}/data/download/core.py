import torchutil

import {{cookiecutter.project_slug}}


###############################################################################
# Download datasets
###############################################################################


@torchutil.notify('download')
def datasets(datasets={{cookiecutter.project_slug}}.DATASETS):
    """Download datasets"""
    # TODO - download datasets
    pass
