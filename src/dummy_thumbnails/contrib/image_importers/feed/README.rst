==============================================
dummy_thumbnails.contrib.image_importers.feed
=============================================
Feed image importer for ``django-dummy-thumbnails``. Imports photos from
feeds, that support enclosures.

Installation
============
Add ``dummy_thumbnails.contrib.image_importers.feed`` to your
``INSTALLED_APPS`` in the global ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'dummy_thumbnails.contrib.image_importers.feed',
        # ...
    )

Usage
=====
To import 50 dummy images from Flickr `commercialphotos
<https://www.flickr.com/groups/commercialphotos/>`_ feed, type:

.. code-block:: sh

    ./manage.py dummy_thumbnails_import_from_feed

You can provide a custom feed URL and the number of dummy images to import.
To import 100 images from Flickr `nationalgeographic
<https://www.flickr.com/groups/nationalgeographic/>`_ group, type:

.. code-block:: sh

    ./manage.py dummy_thumbnails_import_from_feed \
        "https://api.flickr.com/services/feeds/groups_pool.gne?id=36256495@N00" \
        --limit=100

Configuration
=============
As you have seen, syntax allows to read images from any feed (that supports
enclosures). In your project, you might want to make it easy for developers,
so that they don't have to type the feed URL. Therefore a setting
``DUMMY_THUMBNAILS_FEED_DEFAULT_FEED_URL`` has been introduced. It defaults
to the URL of the `commercialphotos
<https://www.flickr.com/groups/commercialphotos/>`_ group of the Flickr.

.. code-block:: python

    DUMMY_THUMBNAILS_FEED_DEFAULT_FEED_URL = "https://api.flickr.com/" \
                                             "services/feeds/groups_pool.gne" \
                                             "?id=36256495@N00"

Useful to know
==============
See `this link
<https://www.flickr.com/services/api/explore/flickr.urls.lookupGroup>`_ for
finding the ID of the Flickr group.

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
