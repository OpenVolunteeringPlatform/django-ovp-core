==========
OVP Core
==========

.. image:: https://app.codeship.com/core//status?branch=master
.. image:: https://codecov.io/gh/OpenVolunteeringPlatform/django-ovp-core/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/OpenVolunteeringPlatform/django-ovp-core

This module implements core platform functionality, such as skills, causes and addresses.
It also contains child drf classes such as schema generators.

Getting Started
---------------
Installing
""""""""""""""
1. Install django-ovp-core::

    pip install ovp-core

2. Add it to `INSTALLED_APPS` on `settings.py`


Forking
""""""""""""""
If you have your own OVP installation and want to fork this module
to implement custom features while still merging changes from upstream,
take a look at `django-git-submodules <https://github.com/leonardoarroyo/django-git-submodules>`_.

Testing
---------------
To test this module

::

  python ovp_core/tests/runtests.py

Contributing
---------------
Please read `CONTRIBUTING.md <https://github.com/OpenVolunteeringPlatform/django-ovp-users/blob/master/CONTRIBUTING.md>`_ for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
---------------
We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/OpenVolunteeringPlatform/django-ovp-users/tags>`_. 

License
---------------
This project is licensed under the GNU GPLv3 License see the `LICENSE.md <https://github.com/OpenVolunteeringPlatform/django-ovp-users/blob/master/LICENSE.md>`_ file for details
