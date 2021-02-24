#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import find_packages, setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="flakehell",
    version="ez.0.0.1",
    author="",
    author_email="",
    maintainer="",
    maintainer_email="",
    license="MIT",
    url="https://github.com/evgeniyz321/flakehell",
    description="",
    long_description=read("README.md"),
    packages=find_packages(exclude=["tests", "docs"]),
    python_requires=">=3.5",
    install_requires=[
        "colorama",
        "entrypoints",
        "flake8>=3.8.0",
        "pygments",
        "toml",
        "urllib3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={"flakehell": ["flakehell:entrypoint"]},
)
