import os
import random
import re
from pathlib import Path

DATFILES = (Path(__file__) / '..' / 'datfiles').resolve()


def _get_files():
    files = os.listdir(DATFILES)
    files.remove('LICENSE')
    return [DATFILES / file for file in files]


def fortune():
    paths = _get_files()
    fortunes = []
    for path in paths:
        with open(path, 'r') as f:
            text = re.split(r'[\n|\r\n]%[\n|\r\n]', f.read())
        text = [fortune for fortune in text if fortune.strip('\n\r')]
        fortunes += text
    return random.choice(fortunes)
