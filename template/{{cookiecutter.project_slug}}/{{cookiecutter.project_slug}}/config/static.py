"""Config parameters whose values depend on other config parameters"""
import {{cookiecutter.project_slug}}


###############################################################################
# Directories
###############################################################################


# Location to save dataset partitions
PARTITION_DIR = {{cookiecutter.project_slug}}.ASSETS_DIR / 'partitions'

# Default checkpoint for generation
DEFAULT_CHECKPOINT = {{cookiecutter.project_slug}}.ASSETS_DIR / 'checkpoints'

# Default configuration file
DEFAULT_CONFIGURATION = {{cookiecutter.project_slug}}.ASSETS_DIR / 'configs' / '{{cookiecutter.project_slug}}.py'
