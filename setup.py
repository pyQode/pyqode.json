#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for pyqode.json
"""
import sys
from setuptools import setup, find_packages
from pyqode.json import __version__
#
# add ``build_ui command`` (optional, for development only)
# this command requires the following packages:
#   - pyqt_distutils
#   - pyqode-uic
#
try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    cmdclass = {}


DESCRIPTION = 'Adds JSon support to pyqode.core'


def readme():
    if 'bdist_deb' in sys.argv:
        return DESCRIPTION
    return str(open('README.rst').read())


setup(
    name='pyqode.json',
    namespace_packages=['pyqode'],
    version=__version__,
    packages=[p for p in find_packages() if 'test' not in p],
    keywords=["JSON widget editor"],
    url='https://github.com/pyQode/pyqode.json',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description=DESCRIPTION,
    long_description=readme(),
    install_requires=['pyqode.core'],
    cmdclass=cmdclass,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Text Editors :: Integrated Development Environments (IDE)'])
