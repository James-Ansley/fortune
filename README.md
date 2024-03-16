# Python Fortune

A simple self-contained clone of fortune. Try it out
with [cowsay](https://github.com/James-Ansley/cowsay)!

## Install

    pip install fortune-python

## Usage

### CLI

Currently, a `fortune` command line program is added on install.

```
fortune
```

This will select a random fortune. Adding the fortune command line arguments
is planned later.

### Programmatic

To use this package, import the `fortune` function and call:

```python
from fortune import fortune

print(fortune())
```

This will produce a random fortune.

# Notes

The fortune data for this package is taken
from [fortune-mod](https://github.com/shlomif/fortune-mod). Please see the
datfiles directory in this repo for their corresponding license.

The offensive fortunes in the 'off' directory are not included in this Python
package. However, the fortunes provided in this package are otherwise provided
as they were in the
original [fortune-mod](https://github.com/shlomif/fortune-mod) repository.
I do not take responsibility for the content of these fortunes.
