from pathlib import Path
import yapecs
import {{cookiecutter.project_slug}}

MODULE = '{{cookiecutter.project_slug}}'

file = Path(__file__)
stem = file.stem

CONFIG = stem

# uncomment to use a separate runs dir
# @yapecs.ComputedProperty(compute_once=True)
# def RUNS_DIR():
#     return {{cookiecutter.project_slug}}.ROOT_DIR / f'runs.{stem}'

#uncomment to use a separate eval dir
# @yapecs.ComputedProperty(compute_once=True)
# def EVAL_DIR():
#     return {{cookiecutter.project_slug}}.ROOT_DIR / f'eval.{stem}'

if hasattr({{cookiecutter.project_slug}}, 'defaults'):

    # # Helper function for formatting floats nicely
    # def format_float(f):
    #     return f'{f:.03f}'.replace('.', '_')

    # Possible values
    hparam0 = [1, 2, 3]
    hparam1 = [4, 5, 6]

    # Perform grid search
    HPARAM0, HPARAM1 = yapecs.grid_search(
        file.parent / f'{stem}.progress',
        hparam0,
        hparam1
    )

    CONFIG += f'-{HPARAM0}-{HPARAM1}'

