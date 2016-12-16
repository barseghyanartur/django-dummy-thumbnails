"""
Defaults module.

- IMAGES_PATH: Path to random images.
"""

import os

__title__ = 'dummy_thumbnails.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IMAGES_PATH',
)

IMAGES_PATH = os.path.join('dummy_thumbnails', 'images', 'mixed')
