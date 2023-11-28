import contextlib

import torch
import torchutil

import NAME


###############################################################################
# Application programming interface
###############################################################################


def run(x, checkpoint=NAME.DEFAULT_CHECKPOINT, gpu=None):
    """

    Arguments
        x
            User input
        checkpoint
            The model checkpoint
        gpu
            The GPU index

    Returns
        y
            System output
    """
    # Get inference device
    device = torch.device('cpu' if gpu is None else f'cuda:{gpu}')

    # Preprocess
    features = preprocess(x)

    # Infer
    logits = infer(features.to(device), checkpoint)

    # Postprocess
    return postprocess(logits)


def from_file(
    input_file,
    checkpoint=NAME.DEFAULT_CHECKPOINT,
    gpu=None):
    """Load from file and process

    Arguments
        input_file
            Input file to process
        checkpoint
            The model checkpoint
        gpu : int
            The GPU index

    Returns
        y
            System output
    """
    # TODO - load from input_file
    x = None

    # Process
    return run(x, checkpoint, gpu)


def from_file_to_file(
    input_file,
    output_file,
    checkpoint=NAME.DEFAULT_CHECKPOINT,
    gpu=None):
    """Process file and save to disk

    Arguments
        input_file
            Input file to process
        output_file
            Corresponding file to save processed input
        checkpoint
            The model checkpoint
        gpu
            The GPU index
    """
    # Load and process
    y = from_file()

    # TODO - save y to output_file
    pass


def from_files_to_files(
    input_files,
    output_files,
    checkpoint=NAME.DEFAULT_CHECKPOINT,
    gpu=None):
    """Process many files and save to disk

    Arguments
        input_files
            Input files to process
        output_files
            Corresponding files to save processed input
        checkpoint
            The model checkpoint
        gpu
            The GPU index
    """
    for input_file, output_file in torchutil.iterator(
        zip(input_files, output_files),
        NAME.CONFIG,
        total=len(input_files)
    ):
        from_file_to_file(input_file, output_file, checkpoint, gpu)


###############################################################################
# System flow
###############################################################################


def preprocess(x):
    """Preprocess user inputs"""
    # TODO - preprocess
    features = None

    return features


def infer(features, checkpoint=NAME.DEFAULT_CHECKPOINT):
    """Model forward pass"""
    # Maybe cache model
    if (
        not hasattr(infer, 'model') or
        infer.checkpoint != checkpoint or
        infer.device != features.device
    ):
        # Initialize model
        model = NAME.Model()

        # Load from disk
        infer.model, *_ = torchutil.checkpoint.load(checkpoint, model)
        infer.checkpoint = checkpoint
        infer.device = features.device

        # Move model to correct device
        infer.model = infer.model.to(infer.device)

    with inference_context(infer.model):

        # Infer
        return infer.model(features)


def postprocess(logits):
    """Postprocess logits to produce output"""
    # TODO - postprocess logits
    y = None

    return y


###############################################################################
# Utilities
###############################################################################


@contextlib.contextmanager
def inference_context(model):
    device_type = next(model.parameters()).device.type

    # Prepare model for evaluation
    model.eval()

    # Turn off gradient computation; turn on mixed precision
    with torch.inference_mode(), torch.autocast(device_type):
        yield

    # Prepare model for training
    model.train()
