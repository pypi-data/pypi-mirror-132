|PyPI version| |DOI| |Total alerts| |Language grade: Python| |PyPi
downloads|

flexion
=======

Applying declination and conjugation rules to lemmata.

Warning
-------

Software is **not** production ready and requires more unit testing.

Bender Rule
-----------

The software was developed for processing German-language texts (lang:
de).

Installation in another project
-------------------------------

The ``flexion`` `git repo <http://github.com/ulf/flexion>`__ is
available as `PyPi package <https://pypi.org/project/flexion>`__

.. code:: sh

   pip install flexion

Download a Transducer model

::

   python scripts/download_transducer.py --model=smor

Download demo data for unit tests

::

   mkdir tmp
   wget -O tmp/de_hdt-ud-dev.conllu https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/master/de_hdt-ud-dev.conllu 

Usage
-----

.. code:: py

   import flexion
   import io
   import conllu

   # read CoNLL-U data
   iowrapper = io.open("tmp/de_hdt-ud-dev.conllu", "r", encoding="utf-8")
   dat = [s for s in conllu.parse_incr(iowrapper)]

   # select a sentence examples
   print(dat[5].metadata.get('text'))
   # '" Diesen Gerüchten liegt eine unseriöse Recherche zugrunde .'

   # Generate augmentations
   lemma = "Gerücht"
   substitute = "Spekulation"
   augmentations = flexion.replace(lemma, substitute, dat[5])
   print(augmentations)
   # ['" Diesen Spekulationen liegt eine unseriöse Recherche zugrunde.']

Appendix
--------

Install a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt --no-cache-dir
   pip install -r requirements-dev.txt --no-cache-dir

   # jupyter notebooks
   pip install -r requirements-demo.txt --no-cache-dir
   python -m spacy download de_core_news_lg

(If your git repo is stored in a folder with whitespaces, then don’t use
the subfolder ``.venv``. Use an absolute path without whitespaces.)

Python commands
~~~~~~~~~~~~~~~

-  Jupyter for the examples: ``jupyter lab``
-  Check syntax:
   ``flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')``
-  Run Unit Tests: ``PYTHONPATH=. pytest``

Publish

.. code:: sh

   pandoc README.md --from markdown --to rst -s -o README.rst
   python setup.py sdist 
   twine upload -r pypi dist/*

Clean up
~~~~~~~~

.. code:: sh

   find . -type f -name "*.pyc" | xargs rm
   find . -type d -name "__pycache__" | xargs rm -r
   rm -r .pytest_cache
   rm -r .venv

Support
~~~~~~~

Please `open an issue <https://github.com/ulf/flexion/issues/new>`__ for
support.

Contributing
~~~~~~~~~~~~

Please contribute using `Github
Flow <https://guides.github.com/introduction/flow/>`__. Create a branch,
add commits, and `open a pull
request <https://github.com/ulf/flexion/compare/>`__.

.. |PyPI version| image:: https://badge.fury.io/py/flexion.svg
   :target: https://badge.fury.io/py/flexion
.. |DOI| image:: https://zenodo.org/badge/441439427.svg
   :target: https://zenodo.org/badge/latestdoi/441439427
.. |Total alerts| image:: https://img.shields.io/lgtm/alerts/g/ulf/flexion.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/ulf/flexion/alerts/
.. |Language grade: Python| image:: https://img.shields.io/lgtm/grade/python/g/ulf/flexion.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/ulf/flexion/context:python
.. |PyPi downloads| image:: https://img.shields.io/pypi/dm/flexion
   :target: https://img.shields.io/pypi/dm/flexion
