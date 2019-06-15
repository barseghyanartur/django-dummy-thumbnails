"""
Base module.

- ABSOLUTE_IMAGES_PATH: Path to random images.
- OPTIONS: List of images to choose from.
- get_random_image: Get a random image from the path given.
"""
import codecs
import os
import random

from django.conf import settings

from six import BytesIO

from .settings import IMAGES_PATH, VERIFY_IMAGES

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
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

OPTIONS = []

try:
    # If verify images is set to True, we need to verify images (existence,
    # validity).
    if VERIFY_IMAGES:
        for filename in os.listdir(ABSOLUTE_IMAGES_PATH):
            abs_path = os.path.join(ABSOLUTE_IMAGES_PATH, filename)

            # We need files only; directories are skipped.
            if os.path.isfile(abs_path):
                image_file = codecs.open(abs_path, mode='rb')
                buf = BytesIO(image_file.read())
                image_file.close()

                # Check if it's an image
                try:
                    image = Image.open(buf)

                    try:
                        image.verify()
                        OPTIONS.append(abs_path)
                    except Exception:
                        continue

                except IOError:
                    continue

    # Otherwise, just add files to the list.
    else:
        for filename in os.listdir(ABSOLUTE_IMAGES_PATH):
            abs_path = os.path.join(ABSOLUTE_IMAGES_PATH, filename)
            if os.path.isfile(abs_path):
                OPTIONS.append(abs_path)
except (IOError, OSError):
    pass


def get_random_image(abspath=True):
    """Get random image.

    :param bool abspath: If set to True, absolute path is returned.
    :return str: Path to the file.
    """
    random_image = random.randint(0, len(OPTIONS) - 1)
    image_path = OPTIONS[random_image]

    if abspath:
        return os.path.join(ABSOLUTE_IMAGES_PATH, image_path)
    else:
        return image_path
