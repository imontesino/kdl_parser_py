#!/usr/bin/env python
import pathlib
from itertools import chain
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

package_name = 'kdl_parser_py'


# This call to setup() does all the work
setup(
    name=package_name,
    author="Ignacio Montesino",
    author_email="monte.igna@gmail.com",
    version="0.1",
    description="Create PyKDL chains from URDF robot descriptions",

    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ignamonte',
    maintainer_email='monte.igna@gmail.com',
    long_description=README,
    long_description_content_type="text/markdown",
    license="BSD",
    install_requires=[
        #"PyKDL>=1.4.0",
        "PyYAML>=5.02",
        "setuptools>=45.2.0"
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
