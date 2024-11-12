# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in facebook/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('facebook/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='facebook',
    version=version,
    description='Integrating ERPNext with facebook',
    author='Arpit Jain',
    author_email='arpit.j@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
