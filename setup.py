#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from load_template import __author__, __version__

setup(
    name="load-template",
    author=__author__,
    description="Create a file from the template with the variables.",
    version=__version__,
    license="MIT License",
    url="https://github.com/alice1017/load-template",
    entry_points={
        "console_scripts": [
            "load-template=load_template.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: Alpha",
        "Programming Language :: Python :: 2.7"
    ]
)
