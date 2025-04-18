import json
import random

import {{cookiecutter.project_slug}}


def datasets(datasets={{cookiecutter.project_slug}}.DATASETS):
    """Partition datasets"""
    for dataset in datasets:

        # Random seed
        random.seed({{cookiecutter.project_slug}}.RANDOM_SEED)

        # TODO - make partition dictionary
        partition = {'train': [], 'valid': [], 'test': []}

        # Save to disk
        file = {{cookiecutter.project_slug}}.PARTITION_DIR / f'{dataset}.json'
        file.parent.mkdir(exist_ok=True, parents=True)
        with open(file, 'w') as file:
            json.dump(partition, file, indent=4)
