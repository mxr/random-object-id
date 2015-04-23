import re
import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

init_path = 'random_object_id/__init__.py'
version = re.search('"([0-9\.]+)"', read(init_path)).group(1)

long_description = read('README.rst')

setup(
    name='random-object-id',
    packages=['random_object_id'],
    entry_points={
        'console_scripts': [
            'random_object_id=random_object_id.random_object_id:main',
        ],
    },
    version=version,
    description='Generate a random MongoDB ObjectId.',
    long_description=long_description,
    author='Max Rozentsveyg',
    author_email='maxr@outlook.com',
    license='MIT',
    keywords='random test MongoDB mongo ObjectId',
    url='https://github.com/mxr/random-object-id',
)
