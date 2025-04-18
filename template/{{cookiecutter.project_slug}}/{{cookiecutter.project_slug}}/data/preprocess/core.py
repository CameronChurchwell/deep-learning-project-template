import torchutil

import {{cookiecutter.project_slug}}


###############################################################################
# Preprocess
###############################################################################


@torchutil.notify('preprocess')
def datasets(datasets):
    """Preprocess a dataset

    Arguments
        name - string
            The name of the dataset to preprocess
    """
    for dataset in datasets:
        input_directory = {{cookiecutter.project_slug}}.DATA_DIR / dataset
        output_directory = {{cookiecutter.project_slug}}.CACHE_DIR / dataset

        # TODO - Perform preprocessing
        raise NotImplementedError
