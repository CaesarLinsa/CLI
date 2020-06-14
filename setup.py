#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name="cli",
    version="1.0",
    author="caesarlinsa",
    author_email="Caesar_Linsa@163.com",
    description=("this is command line package"),
    license="MIT",
    packages=['cli'],

    install_requires=[
        'argparse>=1.4.0',
    ]
)
