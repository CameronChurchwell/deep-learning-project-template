import json
import warnings
from pathlib import Path

# import accelerate
import numpy as np
import torch
import torchaudio

import NAME


###############################################################################
# Dataset
###############################################################################


class Dataset(torch.utils.data.Dataset):

    def __init__(
        self,
        name_or_files,
        partition=None,
        features=['audio'],
        memory_caching=NAME.MEMORY_CACHING):
        self.features = features
        self.metadata = Metadata(
            name_or_files,
            partition=partition)
        self.cache = self.metadata.cache_dir
        self.stems = self.metadata.stems
        self.audio_files = self.metadata.audio_files
        self.lengths = self.metadata.lengths
        self.memory_caching = False
        if memory_caching:
            self.memory_cache = []
            for index in range(0, len(self)):
                self.memory_cache.append(self[index])
        self.memory_caching = memory_caching

    def __getitem__(self, index):
        """Retrieve the indexth item"""

        if self.memory_caching:
            return self.memory_cache[index]

        stem = self.stems[index]

        feature_values = []
        if isinstance(self.features, str):
            self.features = [self.features]
        for feature in self.features:

            # Load audio
            if feature == 'audio':
                audio = NAME.load.audio(self.audio_files[index])
                feature_values.append(audio)

            # Add stem
            elif feature == 'stem':
                feature_values.append(stem)

            # Add filename
            elif feature == 'audio_file':
                feature_values.append(self.audio_files[index])

            # Add length
            elif feature == 'length':
                try:
                    feature_values.append(feature_values[-1].shape[-1])
                except AttributeError:
                    feature_values.append(len(feature_values[-1]))

            # Add input representation
            else:
                feature_values.append(
                    torch.load(self.cache / f'{stem}-{feature}.pt', weights_only=True))

        return feature_values

    def __len__(self):
        """Length of the dataset"""
        return len(self.stems)

    def buckets(self):
        """Partition indices into buckets based on length for sampling"""
        # Get the size of a bucket
        size = len(self) // NAME.BUCKETS

        # Get indices in order of length
        indices = np.argsort(self.lengths)
        lengths = np.sort(self.lengths)

        # Split into buckets based on length
        buckets = [
            np.stack((indices[i:i + size], lengths[i:i + size])).T
            for i in range(0, len(self), size)]

        # Concatenate partial bucket
        if len(buckets) == NAME.BUCKETS + 1:
            residual = buckets.pop()
            buckets[-1] = np.concatenate((buckets[-1], residual), axis=0)

        return buckets


###############################################################################
# Utilities
###############################################################################


class Metadata:

    def __init__(
        self,
        name_or_files,
        partition=None,
        overwrite_cache=False):
        """Create a metadata object for the given dataset or sources"""
        lengths = {}

        # Create dataset from string identifier
        if isinstance(name_or_files, str):
            self.name = name_or_files
            self.data_dir = NAME.DATA_DIR / self.name
            self.cache_dir = NAME.CACHE_DIR / self.name

            if not self.cache_dir.exists():
                self.cache_dir.mkdir()

            # Get stems corresponding to partition
            partition_dict = NAME.load.partition(self.name)
            if partition is not None:
                self.stems = partition_dict[partition]
                lengths_file = self.cache_dir / f'{partition}-lengths.json'
            else:
                self.stems = sum(partition_dict.values(), start=[])
                lengths_file = self.cache_dir / f'lengths.json'

            # Get audio filenames
            self.audio_files = [
                self.data_dir / (stem + '.wav') for stem in self.stems]

            # Maybe remove previous cached lengths
            if overwrite_cache:
                lengths_file.unlink(missing_ok=True)

            # Load cached lengths
            if lengths_file.exists():
                with open(lengths_file, 'r') as f:
                    lengths = json.load(f)

        # Create dataset from a list of audio filenames
        else:
            self.name = '<list of files>'
            self.audio_files = name_or_files
            self.stems = [
                Path(file).parent / Path(file).stem
                for file in self.audio_files]
            self.cache_dir = None

        if not lengths:

            # Compute length in frames
            for stem, audio_file in zip(self.stems, self.audio_files):
                info = torchaudio.info(audio_file)
                length = int(
                    info.num_frames * (NAME.SAMPLE_RATE / info.sample_rate)
                ) // NAME.HOPSIZE

                lengths[stem] = length

            # Maybe cache lengths
            if self.cache_dir is not None:
                with open(lengths_file, 'w+') as file:
                    json.dump(lengths, file)

        # Match ordering
        (
            self.audio_files,
            self.stems,
            self.lengths
            ) = zip(*[
            (file, stem, lengths[stem])
            for file, stem in zip(self.audio_files, self.stems)
            if stem in lengths
        ])

    def __len__(self):
        return len(self.stems)