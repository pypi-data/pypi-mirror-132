========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-selenium-webdriver-extender/badge/?style=flat
    :target: https://python-selenium-webdriver-extender.readthedocs.io/
    :alt: Documentation Status

.. |requires| image:: https://requires.io/github/15minutOdmora/python-selenium-webdriver-extender/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/15minutOdmora/python-selenium-webdriver-extender/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/selenium-webdriver-extender.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/selenium-webdriver-extender

.. |wheel| image:: https://img.shields.io/pypi/wheel/selenium-webdriver-extender.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/selenium-webdriver-extender

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/selenium-webdriver-extender.svg
    :alt: Supported versions
    :target: https://pypi.org/project/selenium-webdriver-extender

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/selenium-webdriver-extender.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/selenium-webdriver-extender

.. |commits-since| image:: https://img.shields.io/github/commits-since/15minutOdmora/python-selenium-webdriver-extender/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/15minutOdmora/python-selenium-webdriver-extender/compare/v0.0.0...master



.. end-badges

Selenium webdriver extender for simplifying webdriver installation and managment, webdriver execution and more.

* Free software: MIT license

Installation
============

::

    pip install selenium-webdriver-extender

You can also install the in-development version with::

    pip install https://github.com/15minutOdmora/python-selenium-webdriver-extender/archive/master.zip


Documentation
=============


https://python-selenium-webdriver-extender.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
