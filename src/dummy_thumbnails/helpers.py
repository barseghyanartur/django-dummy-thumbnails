"""
Helpers module.

- prepare_dirs_and_symlinks: Prepare dirs and symlinks.
"""

import os

from django.conf import settings

__title__ = 'dummy_thumbnails.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('prepare_dirs_and_symlinks',)


def prepare_dirs_and_symlinks(create_dirs=False):
    """Prepare dirs and symlinks.

    :param bool create_dirs: If set to True, dirs are created.
    """
    # What we shall do is to create dirs and make a symbolic link.
    if create_dirs:
        __dirs = (
            os.path.join('examples', 'db'),
            os.path.join('examples', 'logs'),
            os.path.join('examples', 'tmp'),
            os.path.join('examples', 'media', 'static'),
            os.path.join('examples', 'static')
        )
        for __dir in __dirs:
            try:
                os.makedirs(os.path.abspath(__dir))
            except OSError:
                pass

    try:
        os.symlink(
            os.path.join(settings.STATIC_ROOT,
                         'dummy_thumbnails',
                         'images',
                         'mixed'),
            os.path.join(settings.MEDIA_ROOT, 'mixed')
        )
    except OSError:
        pass
