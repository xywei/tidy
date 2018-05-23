#!/usr/bin/env python

__copyright__ = "Copyright (C) 2018 Xiaoyu Wei"

__license__ = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

version_dict = {}
init_filename = "tidy/version.py"
with open(init_filename, 'r') as init_file:
    exec(compile(init_file.read(), init_filename, mode='exec'),
         version_dict)

setup(name='Tidy',
      version=version_dict['VERSION_TEXT'],
      description='Minimalistic document management system',
      long_description=open("README.rst", "rt").read(),
      author='Xiaoyu Wei',
      author_email='xywei@pm.me',
      license="GPLv3",
      url='https://tidy.readthedocs.io/',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Other Audience',

          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: SQL',

          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: BSD',
          'Operating System :: POSIX :: Linux',

          'Topic :: Database',
          'Topic :: System :: Archiving',
          'Topic :: Utilities',
      ],

      packages=find_packages(),

      scripts=['tidy/cli/tid', ],

      install_requires=[
          'docopt',
          'ocrmypdf',
      ],

      extras_require={
          'dev': [
              'autopep8',
              'pytest',
              'sphinx',
              'sphinx_rtd_theme',
          ],
      },
      )
