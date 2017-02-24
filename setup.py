# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:

    readme = f.read()

with open('LICENSE') as f:

    license = f.read()

setup(

    name='itebooks',

    version='0.3.1',

    description='Python wrapper for it-ebooks-api.',

    long_description=readme,

    author='Akshay',

    author_email='akshayjr69@gmail.com',

    url='https://github.com/aksbuzz/pyebooks',

    license=license,

    packages=find_packages(exclude=('tests', 'docs'))
)