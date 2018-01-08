"""
Settings module.

- IMAGES_PATH: Path to random images.
- VERIFY_IMAGES: If set to True, images are verified.
"""

from .conf import get_setting

__title__ = 'dummy_thumbnails.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IMAGES_PATH',
    'VERIFY_IMAGES',
)

IMAGES_PATH = get_setting('IMAGES_PATH')
VERIFY_IMAGES = get_setting('VERIFY_IMAGES')
