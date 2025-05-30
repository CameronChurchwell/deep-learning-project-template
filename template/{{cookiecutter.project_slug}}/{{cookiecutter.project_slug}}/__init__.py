###############################################################################
# Configuration
###############################################################################


# Default configuration parameters to be modified
from .config import defaults

# Modify configuration
import yapecs
yapecs.configure('{{cookiecutter.project_slug}}', defaults)
del defaults # use {{cookiecutter.project_slug}}.defaults as a lock for grid search

# Import configuration parameters
from .config.defaults import *
from .config.static import *


###############################################################################
# Module imports
###############################################################################


from .core import *
from .model import Model
from . import train
from . import data
from . import evaluate
from . import load
