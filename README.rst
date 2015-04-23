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

Python 2.7 and 3.2+. See the Travis button above for the full breakdown.

Usage
-----

::

    Usage: random-object-id.py [options]

    Options:
      -h, --help      show this help message and exit
      -l, --longform  prints the ID surrounded by ObjectId(...)

Examples
--------

::

    $ python random-object-id/random-object-id.py
    55348611a56c10449ab80a4f
    $ python random-object-id/random-object-id.py -l
    ObjectId("553486125ed592a10c4e8e6b")

Coming soon
-----------

You’ll be able to install this from pip

.. |Build Status| image:: https://travis-ci.org/mxr/random-object-id.svg?branch=master
   :target: https://travis-ci.org/mxr/random-object-id
