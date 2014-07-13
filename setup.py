#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, microLearner development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

# The PACKAGE is the top-level folder containing the __init__.py module
# that should be in the same directory as your setup.py file
PACKAGE = "microLearner"
# The NAME is what people will refer to your software as,
# the name under which your software is listed in PyPI and
# under which users will install it (for example, pip install NAME)
NAME = "microLearner"
DESCRIPTION = "Python package for ncRNA annotation"
AUTHOR = "microLearner development team"
AUTHOR_EMAIL = "zhenjiang.xu@gmail.com"
URL = "https://github.com/RNAer/microLearner"
VERSION = __import__(PACKAGE).__version__

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Get the long description from the relevant file
with open('README.rst') as f:
    long_description = f.read()

setup(
    name=NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=VERSION,

    # What does your project relate to?
    keywords=['Microbiome', 'Machine Learning', 'Bioinformatics'],

    description=DESCRIPTION,

    long_description=long_description,

    # The project's main homepage.
    url=URL,

    # Author details
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Bioinformatician',

        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=['numpy >= 1.7',
                      'scipy >= 0.13.0',
                      'matplotlib >= 1.1.0',
                      'scikit-learn',
                      'click',
                      # 'biom',
                      'pandas',
                      'future'],
    extras_require={'test': ["nose >= 0.10.1", "pep8", "flake8"],
                    'doc':  ["Sphinx >= 1.2.2", "sphinx-bootstrap-theme"]},

    # Include additional files into the package
    include_package_data=True,

    # If there are data files included in your packages that need to be
    # installed, specify them here. If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'microLearner': ['data/*'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'microLearner=microLearner.cmd:microLearner',
        ],
    },

    test_suite='nose.collector'
)
