#!/usr/bin/env python

"""
Setup script for curmit.
"""

import setuptools

from curmit import __project__, CLI

# Touch the README, it will be generated on release
README = 'README.rst'
import os
if not os.path.exists(README):
    open(README, 'wb').close()
CHANGES = 'CHANGES.md'

setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="Grabs text from a URL and commits it.",
    url='http://github.com/jacebrowning/curmit',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [CLI + ' = curmit:main']},

    long_description=(open(README).read() + '\n' +
                      open(CHANGES).read()),
    license='LGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Version Control',
    ],

    install_requires=["html2text==3.200.3"],
)
