#!/usr/bin/env python
import setuptools
from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), 'r') as f:
    long_description = f.read()

setup(
    name = 'ic-py',
    version = '0.0.8',
    description = 'Python Agent Library for the Internet Computer',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/rocklabs-io/ic-py',
    author = 'Rocklabs',
    author_email = 'ccyanxyz@gmail.com',
    keywords = 'dfinity ic agent',
    install_requires = ['requests>=2.22.0', 'ecdsa>=0.18.0b1', 'cbor2>=5.4.2', 'leb128>=1.0.4', 'waiter>=1.2'],
    py_modules = ['ic'],
    package_dir = { 'ic': "ic" },
    packages = setuptools.find_packages(where='./'),
    include_package_data = True
)
