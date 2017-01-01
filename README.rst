Random ObjectId |Build Status| |Wheel Badge|
============================================

Motivation
----------

This is a toy project without any outlandish goals. Occasionally I needed a MongoDB ObjectID for a unit test. This saves a DB query, starting ``mongo`` locally, writing more than a line of Python, or visiting a website. I also wanted to learn more about writing & deploying Python packages.

Dependencies
------------

None. The ``dev_requirements.txt`` file is used for dependencies needed to contribute to the project.

Supports
--------

Python 2.7 and 3.2+. See ``.travis.yml`` here_.

Installation
------------

::

    pip install random-object-id

Usage
-----

::

    $ random_object_id -h
    usage: random_object_id [-h] [-l]

    Generate a random MongoDB ObjectId

    optional arguments:
      -h, --help      show this help message and exit
      -l, --longform  prints the ID surrounded by ObjectId("...")

Examples
--------

::

    $ random_object_id
    55348611a56c10449ab80a4f
    $ random_object_id -l
    ObjectId("553486125ed592a10c4e8e6b")

.. |Build Status| image:: https://img.shields.io/travis/mxr/random-object-id.svg?maxAge=2592000
   :target: https://travis-ci.org/mxr/random-object-id
.. |Wheel Badge| image:: https://img.shields.io/pypi/wheel/random-object-id.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/random-object-id/
   :alt: Wheel Status
.. _here: https://github.com/mxr/random-object-id/blob/master/.travis.yml
