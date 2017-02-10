=======================
django-dummy-thumbnails
=======================
Dummy thumbnails for `most popular <Supported thumbnailers_>`_ Django
thumbnail generators.

There are times when you have a database of a Django site and you need to
quickly start it up to fix/develop, but then you realise that images are
missing and you need to have images, because either your layout is broken or,
in the worst case, entire site is broken (500). This library has been written
for developers in order to avoid above mentioned problems in the shortest way
possible, with least efforts possible.

Prerequisites
=============
- Django 1.8, 1.9, 1.10, 1.11
- Python 2.7, 3.4, 3.5, 3.6

Although `django-dummy-thumbnails` is not being tested against older versions
of Django, tests do pass with Django versions 1.5, 1.6 and 1.7.

Installation
============
(1) Install in your virtual environment

    Latest stable version from PyPI:

    .. code-block:: sh

        pip install django-dummy-thumbnails

    Latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/django-dummy-thumbnails/archive/stable.tar.gz

(2) Add ``dummy_thumbnails`` to your ``INSTALLED_APPS`` in the
    global ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'dummy_thumbnails',
            # ...
        )

(3) Specify a custom path to your images directory:

    .. code-block:: python

        DUMMY_THUMBNAILS_IMAGES_PATH = '/home/path/to/images/'

    This should be a directory inside your media directory of your Django
    project. Otherwise Django would raise a ``SuspiciousOperation`` exception.
    In order not to duplicate tons of files for each project, you are advised
    to create symlinks to the images directory in the media directory of your
    Django project.

    .. code-block:: sh

        ln -s /home/path/to/images /home/repos/your-django-project/media

    If you prefer to use included `public domain images
    <https://github.com/barseghyanartur/django-dummy-thumbnails/tree/master/src/dummy_thumbnails/static/dummy_thumbnails/images/mixed>`_,
    run the following management commands:

    .. code-block:: sh

        ./manage.py collectstatic --noinput
        ./manage.py dummy_thumbnails_symlink_dummy_images

    And specify the following path:

    .. code-block:: python

        DUMMY_THUMBNAILS_IMAGES_PATH = os.path.join(MEDIA_ROOT, 'mixed')

Usage
=====
Common usage examples.

Replace broken images with dummy ones
-------------------------------------
That's what it's all about - replacing the broken images with dummy ones.

.. note:: You should **never** use this in production. All the changes
          mentioned above and below are supposed to be applied to
          **development** settings only.

Supported thumbnailers
~~~~~~~~~~~~~~~~~~~~~~
Most popular image thumbnailers for Django (`django-imagekit`_,
`sorl-thumbnail`_ and `easy-thumbnails`_) are supported. If you can't find
your favourite thumbnailer, open an issue or consider making a pull request.

django-imagekit
^^^^^^^^^^^^^^^
Integration with `django-imagekit
<https://pypi.python.org/pypi/django-imagekit>`_.

Modify your settings in the following way:

(1) Add ``imagekit``, ``dummy_thumbnails`` and
    ``dummy_thumbnails.contrib.thumbnailers.django_imagekit.generatorlibrary``
    to the ``INSTALLED_APPS``:

    .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'imagekit',
            'dummy_thumbnails',
            'dummy_thumbnails.contrib.thumbnailers.django_imagekit.generatorlibrary',
            # ...
        ]

(2) If you are using the included public domain images, don't forget to collect
    the static files and create a symlink:

    .. code-block:: sh

        ./manage.py collectstatic --noinput
        ./manage.py dummy_thumbnails_symlink_dummy_images

(3) Now the following would work:

    .. code-block:: html

        {% load imagekit %}

        {% thumbnail '640x480' 'None1' %}
        {% thumbnail '480x640' 'None2' %}
        {% thumbnail '200x200' 'None3' %}

sorl-thumbnail
^^^^^^^^^^^^^^
Integration with `sorl-thumbnail
<https://pypi.python.org/pypi/sorl-thumbnail>`_.

Modify your settings in the following way:

(1) Add ``sorl.thumbnail`` and ``dummy_thumbnails`` to the ``INSTALLED_APPS``:

    .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'sorl.thumbnail',
            'dummy_thumbnails',
            # ...
        ]

(2) Set the dummy thumbnail engine as ``THUMBNAIL_ENGINE``:

    .. code-block:: python

        THUMBNAIL_ENGINE = 'dummy_thumbnails.contrib.sorl_thumbnail.engines.DummyThumbnailsEngine'

(3) If you are using the included public domain images, don't forget to collect
    the static files and create a symlink:

    .. code-block:: sh

        ./manage.py collectstatic --noinput
        ./manage.py dummy_thumbnails_symlink_dummy_images

(4) Now the following would work:

    .. code-block:: html

        {% load thumbnail %}

        {% thumbnail 'None1' "640x480" crop="center" as im %}
            <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}" />
        {% endthumbnail %}

        {% thumbnail 'None2' "480x640" crop="center" as im %}
            <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}" />
        {% endthumbnail %}

        {% thumbnail 'None3' "200x200" crop="center" as im %}
            <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}" />
        {% endthumbnail %}

easy-thumbnails
^^^^^^^^^^^^^^^
Integration with `easy-thumbnails
<https://pypi.python.org/pypi/easy-thumbnails>`_.

Modify your settings in the following way:

(1) Add ``easy_thumbnails`` and ``dummy_thumbnails`` to the ``INSTALLED_APPS``:

    .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'easy_thumbnails',
            'dummy_thumbnails',
            # ...
        ]

(2) Add dummy thumbnail generator to ``THUMBNAIL_SOURCE_GENERATORS``:

    .. code-block:: python

        THUMBNAIL_SOURCE_GENERATORS = (
            'dummy_thumbnails.contrib.thumbnailers.easy_thumbnails.source_generators.dummy_thumbnail',
        )

(3) If you are using the included public domain images, don't forget to collect
    the static files and create a symlink:

    .. code-block:: sh

        ./manage.py collectstatic --noinput
        ./manage.py dummy_thumbnails_symlink_dummy_images

(4) Now the following would work:

    .. code-block:: html

        {% load thumbnail %}

        <img src="{% thumbnail 'None1' 640x480 crop %}" alt="" />
        <img src="{% thumbnail 'None2' 480x640 crop %}" alt="" />
        <img src="{% thumbnail 'None3' 200x200 crop %}" alt="" />

Dealing with broken or invalid dummy images
===========================================
Of course, it's always better to have a good working set of dummy images.
However, it might happen that for some reason one of your dummy images
is broken.

The recommended approach is to use a management command
``dummy_thumbnails_verify_dummy_images``, which has been written in order to
verify the dummy images and identify possible problems. It also lets you
remove broken/invalid dummy images.

To remove broken/invalid dummy images with confirmation, type:

.. code-block:: sh

    ./manage.py dummy_thumbnails_verify_dummy_images

To remove broken/invalid dummy images without confirmation, type:

.. code-block:: sh

    ./manage.py dummy_thumbnails_verify_dummy_images --noinput

To just list broken/invalid dummy images without removal, type:

.. code-block:: sh

    ./manage.py dummy_thumbnails_verify_dummy_images --list

Another way to avoid failures is to set the value of
``DUMMY_THUMBNAILS_VERIFY_IMAGES`` to True in your project settings. Beware,
that this slows down the start up time of your Django project, although does
not slow down further rendering of the images.

Demo
====
Run demo locally
----------------
In order to be able to quickly evaluate the `django-dummy-thumbnails`, a demo
app (with a quick installer) has been created (works on Ubuntu/Debian, may
work on other Linux systems as well, although not guaranteed). Follow the
instructions below to have the demo running within a minute.

Grab the latest ``dummy_thumbnails_demo_installer.sh``:

.. code-block:: sh

    wget -O - https://raw.github.com/barseghyanartur/django-dummy-thumbnails/stable/examples/dummy_thumbnails_demo_installer.sh | bash

Open your browser and test the app.

- URL: http://127.0.0.1:8001/

If quick installer doesn't work for you, see the manual steps on running the
`example project
<https://github.com/barseghyanartur/django-dummy-thumbnails/tree/stable/examples>`_.

Importing images from feed
==========================
Imports images from feeds, that support enclosures.

Installation
------------
Add ``dummy_thumbnails.contrib.image_importers.feed`` to your
``INSTALLED_APPS`` in the global ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'dummy_thumbnails.contrib.image_importers.feed',
        # ...
    )

Usage
-----
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
-------------
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

Testing
=======
Simply type:

.. code-block:: sh

    ./runtests.py

or use tox:

.. code-block:: sh

    tox

or use tox to check specific env:

.. code-block:: sh

    tox -e py35

or run Django tests:

.. code-block:: sh

    ./manage.py test dummy_thumbnails --settings=settings.testing

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
