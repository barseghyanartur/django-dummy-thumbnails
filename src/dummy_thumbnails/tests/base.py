"""
Base tests module.

- log_info: Method decorator, logs info about the method (name, return value).
- LOG_INFO: Flag.
- app_setup: Setup the app.
- skip: Method decorator. If used, tests is skipped.
- is_app_setup_completed: Check if app setup has been completed.
- mark_app_setup_as_completed: Mark the app setup as completed.
"""

from __future__ import print_function

import logging

__title__ = 'dummy_thumbnails.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'LOG_INFO',
    'log_info',
    'APP_SETUP',
    'skip',
    'is_app_setup_completed',
    'mark_app_setup_as_completed',
)


LOGGER = logging.getLogger(__name__)

LOG_INFO = True


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        result = func(self, *args, **kwargs)

        LOGGER.info('\n%s', func.__name__)
        LOGGER.info('============================')
        if func.__doc__:
            LOGGER.info('""" %s """', func.__doc__.strip())
        LOGGER.info('----------------------------')
        if result is not None:
            LOGGER.info(result)
        LOGGER.info('\n')

        return result
    return inner


SKIP = False


def skip(func):
    """Simply skip the test."""
    def inner(self, *args, **kwargs):
        """Inner."""
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner


class AppSetup(object):
    """Basic setup class.

    Created in order to avoid the app test data to be initialised
    multiple times.
    """
    def __init__(self):
        self.is_done = False


APP_SETUP = AppSetup()


def is_app_setup_completed():
    """Check if app setup is completed."""
    return APP_SETUP.is_done is True


def mark_app_setup_as_completed():
    """Mark app setup as completed."""
    APP_SETUP.is_done = True
