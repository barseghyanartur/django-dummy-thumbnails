=======================
django-dummy-thumbnails
=======================
Generate dummy thumbnails with most popular Django thumbnail generators.

There are times when you have a database of Django site and you need to
quickly start it up to fix/develop, but then you realise that you have to
have images, because either your layout is broken or, in the worst case,
entire site is broken (500). This library has been written for developers
in order to avoid above mentioned problems in the shortest way possible,
with least efforts possible.

Prerequisites
=============
- Django 1.8, 1.9, 1.10
- Python 2.7, 3.4, 3.5

Installation
============
(1) Install in your virtual environment

    Latest stable version from PyPI:

    .. code-block:: sh

        pip install django-dummy-thumbnails

    Latest stable version from github:

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

    This should be a directory inside your media (or static) directory of your
    Django project. Otherwise Django would raise a ``SuspiciousOperation``
    exception. In order not to duplicate tons of files for each project, you
    are advised to create symlinks to the images directory in the media (or
    static) directory of your Django project.

    .. code-block:: sh

        ln -s /home/path/to/images /home/repos/your-django-project/media

    If you prefer to use included public domain images, run the following
    management commands:

    .. code-block:: sh

        ./manage.py collectstatic --noinput
        ./manage.py dummy_thumbnails_symlink_dummy_images

    And specify the following path

    .. code-block:: python

        DUMMY_THUMBNAILS_IMAGES_PATH = os.path.join(MEDIA_ROOT, 'mixed')

Usage
=====
Common usage examples.

Replace broken images with dummy ones
-------------------------------------
That's what it's all about - replacing the broken images with dummy ones.

Supported thumbnailers
~~~~~~~~~~~~~~~~~~~~~~
A number of most popular image thumbnailers for Django is supported. If you
can't find your favourite thumbnailer, open an issue or consider making a
pull request.

easy_thumbnails
^^^^^^^^^^^^^^^
Integration with `easy_thumbnails
<https://pypi.python.org/pypi/easy-thumbnails>`_.

Modify your settings in the following way:

(1) Add ``dummy_thumbnails`` to the ``INSTALLED_APPS``:

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

(3) If you are using the included images, don't forget to collect the static
    files:

    .. code-block:: sh

        ./manage.py collectstatic --noinput

(4) Now the following would work:

    .. code-block:: html

        {% load thumbnail %}

        <img src="{% thumbnail 'None1' 640x480 crop %}" alt="" />
        <img src="{% thumbnail 'None2' 480x640 crop %}" alt="" />
        <img src="{% thumbnail 'None3' 200x200 crop %}" alt="" />

sorl-thumnail
^^^^^^^^^^^^^
Integration with `sorl-thimbnail
<https://pypi.python.org/pypi/sorl-thumbnail>`_.

Modify your settings in the following way:

(1) Add ``dummy_thumbnails`` to the ``INSTALLED_APPS``:

    .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'sorl_thumbnail',
            'dummy_thumbnails',
            # ...
        ]

(2) Set the dummy thumbnail engine as ``SORL_THUMBNAIL_THUMBNAIL_ENGINE``:

    .. code-block:: python

        SORL_THUMBNAIL_THUMBNAIL_ENGINE = 'dummy_thumbnails.contrib.sorl_thumbnail.engines.DummyThumbnailsEngine'

(3) If you are using the included images, don't forget to collect the static
    files:

    .. code-block:: sh

        ./manage.py collectstatic --noinput

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
