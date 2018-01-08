"""
Settings module.

- DEFAULT_FEED_URL: URL of the default feed.
"""

from .conf import get_setting

__title__ = 'dummy_thumbnails.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DEFAULT_FEED_URL',
)

DEFAULT_FEED_URL = get_setting('DEFAULT_FEED_URL')
