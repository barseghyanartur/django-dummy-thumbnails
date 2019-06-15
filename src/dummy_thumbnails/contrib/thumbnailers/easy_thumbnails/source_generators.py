"""
easy-thumbnails contrib module. Since thumbnail generation in easy-thumbnails
goes through source generators, we should make a new source generator for the
thumbnail generation, which will replace broken thumbnails with dummy ones.
In settings we set patched source generator in ``THUMBNAIL_SOURCE_GENERATORS``
setting.

- dummy_thumbnail: Dummy thumbnails generator for easy-thumbnails.
"""

import codecs
import os

from django.conf import settings as django_settings

from easy_thumbnails.source_generators import pil_image

from six import PY3

from ....base import get_random_image

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.contrib.thumbnailers.easy_thumbnails.' \
            'source_generators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'dummy_thumbnail',
    'load_random_file',
)


def dummy_thumbnail(source, exif_orientation=True, **options):
    """Try to open the source file directly using PIL, ignoring any errors.

    exif_orientation

        If EXIF orientation data is present, perform any required reorientation
        before passing the data along the processing pipeline.

    """
    # Use a BytesIO wrapper because if the source is an incomplete file like
    # object, PIL may have problems with it. For example, some image types
    # require tell and seek methods that are not present on all storage
    # File objects.
    if not (
            source and
            hasattr(source, 'path') and
            (os.path.exists(source.path) or os.path.isfile(source.path))
    ):
        source = load_random_file()

    return pil_image(source, exif_orientation, **options)


def load_random_file():
    """Load random file."""
    # We should load ``ThumbnailFile`` here, since otherwise we might get
    # ``AppRegistryNotReady`` exception.
    from easy_thumbnails.files import ThumbnailFile

    media_root = os.path.abspath(django_settings.MEDIA_ROOT)
    static_root = os.path.abspath(django_settings.STATIC_ROOT)

    random_image = get_random_image()

    if PY3:
        random_file = codecs.open(random_image, mode='rb')
    else:
        random_file = codecs.open(random_image)

    source = ThumbnailFile(random_file.name, random_file)
    source.name = source.file.name \
        .replace(media_root, '') \
        .replace(static_root, '')[1:]

    return source
