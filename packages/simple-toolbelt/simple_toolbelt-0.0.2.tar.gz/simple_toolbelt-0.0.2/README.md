# python-simple-toolbelt

A growing collection of simple utilities functions for Python

## Installation

```bash
pip install simple-toolbelt
```

## Functions

- [path.ensure_dir](#pathensure_dir)

___

#### path.ensure_dir

Create the directories, include subs, if don't exist.

```python
from simple_toolbath.path import ensure_dir

with open(ensure_dir('this/path/to/file.txt'), 'w') as f:
    ...
```
