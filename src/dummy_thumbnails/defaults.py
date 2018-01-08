"""
Defaults module.

- IMAGES_PATH: Path to random images.
- VERIFY_IMAGES: If set to True, images are verified.
"""

import os

__title__ = 'dummy_thumbnails.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IMAGES_PATH',
    'VERIFY_IMAGES',
)

IMAGES_PATH = os.path.join('dummy_thumbnails', 'images', 'mixed')
VERIFY_IMAGES = False
