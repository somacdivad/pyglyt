"""Setup script for pyglyt"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="pyglyt",
    version="0.1.0",
    description="Computational group, graph and set theory in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/somacdivad/pyglyt",
    author="David Amos",
    author_email="somacdivad@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["pyglyt"],
    install_requires=[],
    entry_points={},
)
