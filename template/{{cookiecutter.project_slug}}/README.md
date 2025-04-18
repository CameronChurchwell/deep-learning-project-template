<h1 align="center">Deep learning project template</h1>
<div align="center">

<!-- [![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_slug}}) -->
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<!-- [![Downloads](https://pepy.tech/badge/{{cookiecutter.project_slug}})](https://pepy.tech/project/{{cookiecutter.project_slug}}) -->

</div>


## Table of contents

- [Installation](#installation)
- [Inference](#inference)
    * [Application programming interface](#application-programming-interface)
        * [`{{cookiecutter.project_slug}}.from_text_and_audio`](#{{cookiecutter.project_slug}}from_text_and_audio)
        * [`{{cookiecutter.project_slug}}.from_file`](#{{cookiecutter.project_slug}}from_file)
        * [`{{cookiecutter.project_slug}}.from_file_to_file`](#{{cookiecutter.project_slug}}from_file_to_file)
        * [`{{cookiecutter.project_slug}}.from_files_to_files`](#{{cookiecutter.project_slug}}from_files_to_files)
    * [Command-line interface](#command-line-interface)
- [Training](#training)
    * [Download](#download)
    * [Preprocess](#preprocess)
    * [Partition](#partition)
    * [Train](#train)
    * [Monitor](#monitor)
    * [Evaluate](#evaluate)
- [References](#references)


## Installation

`pip install {{cookiecutter.project_slug}}`


## Inference

```python
import {{cookiecutter.project_slug}}

# TODO - load input
x = None

# Model checkpoint
checkpoint = {{cookiecutter.project_slug}}.DEFAULT_CHECKPOINT

# GPU index
gpu = 0

y = {{cookiecutter.project_slug}}.run(x, checkpoint=checkpoint, gpu=gpu)
```


### Application programming interface

#### `{{cookiecutter.project_slug}}.run`


```
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
```


#### `{{cookiecutter.project_slug}}.from_file`

```
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
```


#### `{{cookiecutter.project_slug}}.from_file_to_file`

```
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
```


#### `{{cookiecutter.project_slug}}.from_files_to_files`

```
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
```


### Command-line interface

```
python -m {{cookiecutter.project_slug}}
    [-h]
    --input_files INPUT_FILES [INPUT_FILES ...]
    --output_files OUTPUT_FILES [OUTPUT_FILES ...]
    [--checkpoint CHECKPOINT]
    [--gpu GPU]

Arguments:
    -h, --help
        show this help message and exit
    --input_files INPUT_FILES [INPUT_FILES ...]
        Input files to process
    --output_files OUTPUT_FILES [OUTPUT_FILES ...]
        Corresponding files to save processed inputs
    --checkpoint CHECKPOINT
        The model checkpoint
    --gpu GPU
        The GPU index
```


## Training

### Download

`python -m {{cookiecutter.project_slug}}.data.download`

Download and uncompress datasets used for training


### Preprocess

`python -m {{cookiecutter.project_slug}}.data.preprocess`

Preprocess datasets


### Partition

`python -m {{cookiecutter.project_slug}}.partition`

Partition datasets. Partitions are saved in `{{cookiecutter.project_slug}}/assets/partitions`.


### Train

`python -m {{cookiecutter.project_slug}}.train --config <config> --gpus <gpus>`

Trains a model according to a given configuration. Uses a list of GPU indices
as an argument, and uses distributed data parallelism (DDP) if more than one
index is given. For example, `--gpus 0 3` will train using DDP on GPUs `0`
and `3`.


### Monitor

Run `tensorboard --logdir runs/`. If you are running training remotely, you
must create a SSH connection with port forwarding to view Tensorboard.
This can be done with `ssh -L 6006:localhost:6006 <user>@<server-ip-address>`.
Then, open `localhost:6006` in your browser.

### Evaluate

```
python -m {{cookiecutter.project_slug}}.evaluate \
    --config <config> \
    --checkpoint <checkpoint> \
    --gpu <gpu>
```

Evaluate a model. `<checkpoint>` is the checkpoint file to evaluate and `<gpu>`
is the GPU index.


## References

