import re

from setuptools import setup

init_contents = open('random_object_id/__init__.py').read()
version = re.search('"([0-9\.]+)"', init_contents).group(1)

with open('README.rst', 'rb') as f:
    long_description = f.read().decode('utf-8')

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
    url='https://github.com/mxr/random-object-id',
)
