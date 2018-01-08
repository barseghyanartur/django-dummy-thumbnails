"""
Feed image importer for ``django-dummy-thumbnails``. Imports photos from
feeds, that support enclosures.

- default_app_config: Default Django app config.
"""

__title__ = 'dummy_thumbnails.contrib.image_importers.feed'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('default_app_config',)

default_app_config = 'dummy_thumbnails.contrib.image_importers.feed.apps.' \
                     'Config'
