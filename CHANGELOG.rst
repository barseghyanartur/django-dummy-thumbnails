Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.2.1
-----
2017-02-21

- Tested against Python 3.6 and Django 1.11.

0.2
---
2017-01-30

- Added a feature to import dummy images from feed.

0.1.10
------
2017-01-26

- Added a ``--list`` option to the management command
  ``dummy_thumbnails_verify_dummy_images``.

0.1.9
-----
2017-01-26

- Minor fixes.

0.1.8
-----
2017-01-25

- Minor fixes.

0.1.7
-----
2017-01-25

- Minor fixes. Skip sub directories when listing files 
  in ``base.get_random_image``.
- Make it possible to detect and remove broken dummy images.

0.1.6
-----
2016-12-23

- Minor fixes in tests against Django 1.8.
- Minor code cleanup.

0.1.5
-----
2016-12-19

- Minor fixes in tests.

0.1.4
-----
2016-12-17

- Minor fixes in tests.

0.1.3
-----
2016-12-16

- Minor fixes/improvements.
- Added ``django-imagekit`` support.

0.1.2
-----
2016-12-15

- Minor fixes in docs and tests.
- Installable demo script added.

0.1.1
-----
2016-12-15

- Include forgotten images (fix in manifest) in the PyPI release.

0.1
---
2016-12-14

- Initial release.
