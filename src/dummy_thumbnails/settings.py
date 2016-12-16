"""
Settings module.

- IMAGES_PATH: Path to random images.
"""

from .conf import get_setting

__title__ = 'dummy_thumbnails.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IMAGES_PATH',
)

IMAGES_PATH = get_setting('IMAGES_PATH')
