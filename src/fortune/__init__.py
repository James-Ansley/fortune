import os
import random
from pathlib import Path

from ._weights import weights

DATFILES = (Path(__file__) / '..' / 'datfiles').resolve()


def _get_files():
    files = os.listdir(DATFILES)
    files.remove('LICENSE')
    return [DATFILES / file for file in files],\
           [weights[file] for file in files]


def fortune():
    files, weights = _get_files()
    path = random.choices(files, weights)[0]
    with open(path) as f:
        data = f.read().strip().strip('%').split('\n%\n')
    return random.choice(data).strip('\n')
