curmit
======

[![Build Status](https://travis-ci.org/jacebrowning/curmit.png?branch=master)](https://travis-ci.org/jacebrowning/curmit)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/curmit/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/curmit?branch=master)
[![PyPI Version](https://badge.fury.io/py/curmit.png)](http://badge.fury.io/py/curmit)

Grabs text from a URL and commits it.

Some possible use cases:

 - collaborate on Markdown/LaTeX using Google Drive
 - incorporate and link to online code snippets 
 - archive the history of a webpage


Requirements
------------

* Python 3.3: http://www.python.org/download/releases/3.3.4/#download
* git: http://git-scm.com/downloads


Installation
------------

curmit can be installed with 'pip':

    pip install curmit

Or directly from the source code:

    git clone https://github.com/jacebrowning/curmit.git
    cd curmit
    python setup.py install


Setup
-----

1. Create a new text file
2. Add the following somewhere in the first few lines:

        curmit: https://docs.google.com/document/d/<DocumentID>/pub?embedded=true


    with your desired URL. An example can be found [here](https://github.com/jacebrowning/curmit/blob/master/docs/sample.md).



Usage
-----

To update every flagged file with the current URL text, commit, and push:

    curmit


**That's it!**
