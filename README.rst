.. image:: https://raw.githubusercontent.com/pyQode/pyQode/master/media/pyqode-banner.png

|

.. image:: https://img.shields.io/pypi/v/pyqode.json.svg
   :target: https://pypi.python.org/pypi/pyqode.json/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/pyqode.json.svg
   :target: https://pypi.python.org/pypi/pyqode.json/
   :alt: Number of PyPI downloads

.. image:: https://img.shields.io/pypi/l/pyqode.python.svg

.. image:: https://travis-ci.org/pyQode/pyqode.json.svg?branch=master
   :target: https://travis-ci.org/pyQode/pyqode.json
   :alt: Travis-CI build status


.. image:: https://coveralls.io/repos/pyQode/pyqode.json/badge.svg?branch=master
   :target: https://coveralls.io/r/pyQode/pyqode.json?branch=master
   :alt: Coverage Status



About
-----

*pyqode.json* adds **JSON** support to `pyQode`_ (syntax highlighter,
navigation panel, code folding,...).

- `Issue tracker`_
- `Wiki`_
- `API reference`_
- `Contributing`_
- `Changelog`_
- `Screenshots`_

Features:
---------

* native syntax highlighter
* specialised code folding detector
* a pre-configured editor: `pyqode.json.widgets.JSONCodeEdit`
* navigation panel (show you the current node and its parents and let you
  navigate between them)

License
-------

pyqode.json is licensed under the **MIT license**.

Requirements
------------

pyqode.json depends on the following libraries:

- python 2.7 or python 3 (>= 3.2)
- pyqode.core


Installation
------------

::

    $ pip install pyqode.json --upgrade

Testing
-------

pyqode.core has a test suite and measure its coverage.

To run the tests, just run ``python setup.py test``

To measure coverage, run::

    python setup.py test -a "--cov pyqode"

To check for PEP8 warnings, install pytest-pep8 and run::

    python setup.py test -a "--pep8 -m pep8"


To run a single test, use ``-a "-- test_file_path.py::test_function"``, e.g.::

    python setup.py test -a "-- test/test_api/test_code_edit.py::test_set_plain_text"


Testing Matrix
++++++++++++++

We test the following combinations on Travis-CI:

+--------------------------+---------+---------+
|                          | PyQt4   | PyQt5   |
+==========================+=========+=========+
| GNU/Linux - Python 2.7   | yes     | no      |
+--------------------------+---------+---------+
| GNU/Linux - Python 3.4   | yes     | yes     |
+--------------------------+---------+---------+


.. _Screenshots: https://github.com/pyQode/pyQode/wiki/Screenshots-and-videos#pyqodejson-screenshots
.. _Issue tracker: https://github.com/pyQode/pyQode/issues
.. _Wiki: https://github.com/pyQode/pyQode/wiki
.. _API reference: http://pyqodejson.readthedocs.org/en/latest/
.. _pyQode: https://github.com/pyQode/pyQode
.. _Changelog: https://github.com/pyQode/pyqode.json/blob/master/CHANGELOG.rst
.. _Contributing: https://github.com/pyQode/pyqode.json/blob/master/CONTRIBUTING.rst
