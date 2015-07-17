#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

PACKAGES = find_packages()


setup(
    name='django-choices',
    version='1.0',
    description=(
        "A handy class for creating 'choices' objects, primarily for use in Django."
    ),
    author='Adam Alton',
    author_email='adamalton@gmail.com',
    url='https://github.com/adamalton/django-choices',
    packages=PACKAGES,
    include_package_data=True,
    # dependencies
    )
