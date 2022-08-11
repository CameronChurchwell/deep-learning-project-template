import json
import random

import NAME


def datasets(datasets, overwrite=False):
    """Partition datasets"""
    for dataset in datasets:

        # Check if partition already exists
        file = NAME.PARTITION_DIR / f'{dataset}.json'
        if file.exists():
            if not overwrite:
                print(f'Not overwriting existing partition {file}')
                continue

        # Random seed
        random.seed(NAME.RANDOM_SEED)

        # TODO - make partition
        partition = None

        # Save to disk
        file.parent.mkdir(exist_ok=True, parents=True)
        with open(file, 'w') as file:
            json.dump(partition, file, ensure_ascii=False, indent=4)