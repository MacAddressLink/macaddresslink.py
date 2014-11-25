#!/usr/bin/env python

from __future__ import with_statement

import re
import sys

try:
    import setuptools as impl
except ImportError:
    import distutils.core as impl

with open('README.md') as ld_file:
    long_description = ld_file.read()

with open('macaddresslink.py') as macaddresslink_source:
    source = macaddresslink_source.read()
    pattern = re.compile(r'''__version__ = ['"](?P<version>[\d.]+)['"]''')
    version = pattern.search(source).group('version')

dependencies = ['requests', 'netifaces']

setup_params = dict(
    name="macaddresslink",
    version=version,
    description="macaddress.link client",
    long_description=long_description,
    author="Shane R. Spencer",
    author_email="shane@bogomip.com",
    url="https://github.com/MacAddressLink/macaddresslink.py",
    license="MIT",
    py_modules=['macaddresslink'],
    #test_suite='tests',
    install_requires=dependencies,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={
        'console_scripts': [
            'macaddresslink = macaddresslink:main',
        ],
    }
)

if __name__ == '__main__':
    impl.setup(**setup_params)
