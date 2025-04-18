# Runs all experiments

# Args
# $1 - index of GPU to use

# Download datasets
python -m {{cookiecutter.project_slug}}.data.download

# Setup experiments
python -m {{cookiecutter.project_slug}}.data.preprocess
python -m {{cookiecutter.project_slug}}.partition

# Train and evaluate
accelerate launch -m {{cookiecutter.project_slug}}.train --config config/config.py
