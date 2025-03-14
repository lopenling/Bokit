# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

setup(
    name='Bokit',
    version='v0.3.1',
    description='Bokit is a Python API that exposes commonly used tools for various Tibetan language workflows.',
    long_description='Bokit is a Python API that exposes commonly used tools for various Tibetan language workflows.',
    url='https://github.com/lopenling/bokit',
    author='Mikko Kotila',
    author_email='mailme@mikkokotila.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='tibetan etl tools',
    packages=find_packages(),
)
