import json
# import torchaudio

import NAME


###############################################################################
# Loading utilities
###############################################################################

# def audio(file):
#     """Load audio from disk"""
#     path = Path(file)
#     if path.suffix.lower() == '.mp3':
#         try:
#             audio, sample_rate = torchaudio.load(path, format='mp3')
#         except RuntimeError:
#             raise RuntimeError(
#                 'Failed to load mp3 file, make sure ffmpeg<=4.3 is installed')
#     else:
#         audio, sample_rate = torchaudio.load(file)

#     # Maybe resample
#     return NAME.resample(audio, sample_rate)

def partition(dataset):
    """Load partitions for dataset"""
    with open(NAME.PARTITION_DIR / f'{dataset}.json') as file:
        return json.load(file)
