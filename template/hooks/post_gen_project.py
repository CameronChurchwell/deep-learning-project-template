import os
from pathlib import Path
import shutil

source_dir = Path(os.getcwd())
target_dir = source_dir.parent

temp_source_dir = source_dir.parent / 'tmp'

shutil.move(source_dir, temp_source_dir)

for p in temp_source_dir.iterdir():
    shutil.move(p, target_dir / p.name)

os.rmdir(temp_source_dir)