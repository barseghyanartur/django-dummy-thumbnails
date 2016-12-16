from __future__ import print_function

import logging

__title__ = 'dummy_thumbnails.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'LOG_INFO',
    'log_info',
    'app_setup',
    'skip',
    'is_app_setup_completed',
    'mark_app_setup_as_completed',
)


logger = logging.getLogger(__name__)

LOG_INFO = True


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        result = func(self, *args, **kwargs)

        logger.info('\n%s', func.__name__)
        logger.info('============================')
        if func.__doc__:
            logger.info('""" %s """', func.__doc__.strip())
        logger.info('----------------------------')
        if result is not None:
            logger.info(result)
        logger.info('\n')

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


app_setup = AppSetup()


def is_app_setup_completed():
    """Check if app setup is completed."""
    return app_setup.is_done is True


def mark_app_setup_as_completed():
    """Mark app setup as completed."""
    app_setup.is_done = True
