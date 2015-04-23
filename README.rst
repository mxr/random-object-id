Random ObjectId |Build Status|
==============================

Motivation
----------

This is a pretty simple project without any outlandish goals. Occasionally I needed a MongoDB ObjectID for a unit test. This saves a query or visiting a website. I also wanted to learn more about writing & deploying Python packages.

Dependencies
------------

None.

Supports
--------

Python 2.7 and 3.2+. See ```.travis.yml```_ for the full breakdown.

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

.. |Build Status| image:: https://travis-ci.org/mxr/random-object-id.svg?branch=master
   :target: https://travis-ci.org/mxr/random-object-id
.. _``.travis.yml``: https://github.com/mxr/random-object-id/blob/master/.travis.yml
