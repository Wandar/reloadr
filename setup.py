# -*- coding: utf-8 -*-

# This file is part of Supernova.
#
# Copyright (C) 2014 Railnova (https://www.railnova.eu)

import os

from setuptools import setup, find_packages
from reloadr import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md') as file:
    long_description = file.read()

setup(name='Reloadr',
      version=__version__,
      description='Hot code reloading tool for Python',
      long_description=long_description,
      author='Hugo Herter',
      author_email='git@hugoherter.com',
      url='https://github.com/hoh/reloadr',
      packages=find_packages(),
      include_package_data=True,
      data_files=[],
      install_requires=[
          'redbaron',
          ],
      license='LGPLv3',
      keywords="reload hot code reloading",
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Programming Language :: Python :: 3.4',
                   'Operating System :: POSIX :: Linux',
                   'Intended Audience :: Developers',
                   ],
      )