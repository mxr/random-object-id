# Random ObjectId

[![Wheel Status](https://img.shields.io/pypi/wheel/random-object-id.svg?maxAge=2592000)](https://pypi.python.org/pypi/random-object-id/)

## Motivation

This is a toy project without any outlandish goals. Occasionally I
needed a MongoDB ObjectID for a unit test. This saves a DB query,
starting `mongo` locally, writing more than a line of Python, or
visiting a website. I also wanted to learn more about writing &
deploying Python packages.

## Dependencies

None

## Supports

py36+. See GitHub workflow [here][GitHub workflow].

## Installation

```console
$ pip install random-object-id
```

## Usage

```console
$ random_object_id -h
usage: random_object_id [-h] [-l]

Generate a random MongoDB ObjectId

optional arguments:
  -h, --help      show this help message and exit
  -l, --longform  prints the ID surrounded by ObjectId("...")
```

```python
from random_object_id import generate

generate()  # => '5ecd3bbf875e60b4166f6699'
```

## Examples

```console
$ random_object_id
55348611a56c10449ab80a4f
$ random_object_id -l
ObjectId("553486125ed592a10c4e8e6b")
```

[GitHub workflow]: https://github.com/mxr/random-object-id/blob/master/.github/workflows/main.yml
