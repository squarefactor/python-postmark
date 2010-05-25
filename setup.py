#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '0.2.0' 

README_FILE = open('README')
try:
    long_description = README_FILE.read()
finally:
    README_FILE.close()

setup(
    name='python-postmark',
    version=VERSION,
    url='http://github.com/squarefactor/python-postmark.git',
    description='Python interface for the Postmark API http://postmarkapp.com',
    long_description=long_description,
    author='Dave Martorana',
    platforms=['any'],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)

