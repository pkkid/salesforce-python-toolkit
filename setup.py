#!/usr/bin/env python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# Written by: David Lanstein ( dlanstein gmail com )
"""
Standard build script.
"""

__docformat__ = 'restructuredtext'

import sys

from setuptools import setup, find_packages

setup(
    name="salesforce-python-toolkit",
    version='0.1.5',
    description="",
    long_description="",
    author="David Lanstein",
    author_email='dlanstein@gmail.com',
    url="http://code.google.com/p/salesforce-python-toolkit/",
    download_url="http://code.google.com/p/salesforce-python-toolkit/downloads/list",
    platforms=['any'],
    install_requires=['suds==0.3.9'],

    license="LGPL",
    packages=find_packages('.'),

    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python'],
    )
