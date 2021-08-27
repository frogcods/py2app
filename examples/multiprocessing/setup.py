"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="MPExample",
    app=['main.py'],
    setup_requires=["py2app"],
)
