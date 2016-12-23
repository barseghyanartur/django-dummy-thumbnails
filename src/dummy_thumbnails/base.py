"""
Base module.

- ABSOLUTE_IMAGES_PATH: Path to random images.
- OPTIONS: List of images to choose from.
- get_random_image: Get a random image from the path given.
"""

import glob
import os
import random

from django.conf import settings

from .settings import IMAGES_PATH

__title__ = 'dummy_thumbnails.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ABSOLUTE_IMAGES_PATH',
    'OPTIONS',
    'get_random_image',
)


if os.path.isabs(IMAGES_PATH):
    ABSOLUTE_IMAGES_PATH = IMAGES_PATH[:]
else:
    ABSOLUTE_IMAGES_PATH = os.path.join(settings.STATIC_ROOT, IMAGES_PATH)

if not ABSOLUTE_IMAGES_PATH.endswith(os.path.sep):
    ABSOLUTE_IMAGES_PATH = os.path.join(ABSOLUTE_IMAGES_PATH, '')
ABSOLUTE_IMAGES_PATH = os.path.join(ABSOLUTE_IMAGES_PATH, '*')

OPTIONS = glob.glob(ABSOLUTE_IMAGES_PATH)


def get_random_image():
    """Get random image."""
    random_image = random.randint(0, len(OPTIONS) - 1)
    return OPTIONS[random_image]
