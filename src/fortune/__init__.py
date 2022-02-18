import os
import random
from pathlib import Path

DATFILES = (Path(__file__) / '..' / 'datfiles').resolve()


def _get_files():
    files = os.listdir(DATFILES)
    files.remove('LICENSE')
    return [DATFILES / file for file in files]


def fortune():
    files = _get_files()
    path = random.choice(files)
    with open(path) as f:
        data = f.read().split('%')
    return random.choice(data).strip('\n')
