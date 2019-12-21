# Copyright 2019 Pascal Audet 
#
# This file is part of RfPy.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""

Licence
-------

Copyright 2019 Pascal Audet 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Installation
------------

Dependencies
++++++++++++

The current version has been tested using **Python3.6 and 3.7** \
Also, the following packages are required:

- `stdb <https://github.com/paudetseis/StDb>`_

Other required packages (e.g., ``obspy``)
will be automatically installed by ``stdb``.

Conda environment
+++++++++++++++++

We recommend creating a custom ``conda`` environment
where ``RfPy`` can be installed along with some of its dependencies.

.. sourcecode:: bash

   conda create -n rfpy python=3.7 obspy -c conda-forge

Activate the newly created environment:

.. sourcecode:: bash

   conda activate rfpy

Install remaining dependencies using ``pip`` inside the ``rfpy`` environment:

.. sourcecode:: bash

   pip install stdb

Installing from Pypi
++++++++++++++++++++

*This option is not available at this time*

Installing from source
++++++++++++++++++++++

- Clone the repository:

.. sourcecode:: bash

   git clone https://github.com/paudetseis/RfPy.git
   cd RfPy

- Install using pip:

.. sourcecode:: bash

   pip install stdb
   pip install .

"""

__version__ = '0.0.1'

__author__ = 'Pascal Audet'

from .rfdata import RFData
from .hk import HkStack
from .harmonics import Harmonics
