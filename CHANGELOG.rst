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
