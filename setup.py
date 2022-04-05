#!/usr/bin/env python
import pathlib
from itertools import chain
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


# This call to setup() does all the work
setup(
    name="kdl_parser",
    author="Ignacio Montesino",
    author_email="monte.igna@gmail.com",
    version="0.1",
    description="Create PyKDL chains from URDF robot descriptions",

    long_description=README,
    long_description_content_type="text/markdown",
    license="BSD",
    install_requires=[
        #"PyKDL>=1.4.0",
        "PyYAML>=5.02",
        "setuptools>=45.2.0"
    ]
)
