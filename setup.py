#!/usr/bin/env python
from setuptools import setup, find_packages


VERSION = 0.1
README = open('README.md').read()


SETUP_REQ = [
    'pytest-runner>=2.8'
]


INSTALL_REQ = [
    'pymongo>=3.4.0',
]


TEST_REQ = [
    'pytest>=2.9.2',
    'pytest-cov>=2.3.0'
]


setup(
    name='ariadne_npdb',
    version=VERSION,
    packages=find_packages(),
    description='ARIADNE Neurophysiology database for MICrONS project',
    long_description=README,
    setup_requires=SETUP_REQ,
    install_requires=INSTALL_REQ,
    tests_require=TEST_REQ,
    include_package_data=True,
    entry_points=dict(
        console_scripts=['ariadne-npdb = ariadne_npdb.cli:main']
    ),
    zip_safe=False
)
