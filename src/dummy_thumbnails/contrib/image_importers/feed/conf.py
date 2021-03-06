"""
Conf module.

- get_setting: Get app setting.
"""

from django.conf import settings

from . import defaults

__title__ = 'dummy_thumbnails.contrib.image_importers.feed.conf'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_setting',)


def get_setting(setting, override=None):
    """Get setting.

    Get a setting from ``dummy_thumbnails`` conf module, falling back to
    the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults to
        None.
    :return: Setting value.
    """
    attr_name = 'DUMMY_THUMBNAILS_FEED_{0}'.format(setting)
    if hasattr(settings, attr_name):
        return getattr(settings, attr_name)
    else:
        if hasattr(defaults, setting):
            return getattr(defaults, setting)
        else:
            return override
