import torch

import {{cookiecutter.project_slug}}


def loader(datasets, partition, gpu=None):
    """Retrieve a data loader"""
    return torch.utils.data.DataLoader(
        dataset={{cookiecutter.project_slug}}.data.Dataset(datasets, partition),
        batch_size={{cookiecutter.project_slug}}.BATCH_SIZE,
        shuffle=partition == 'train',
        num_workers={{cookiecutter.project_slug}}.NUM_WORKERS,
        pin_memory=gpu is not None,
        collate_fn={{cookiecutter.project_slug}}.data.collate)
