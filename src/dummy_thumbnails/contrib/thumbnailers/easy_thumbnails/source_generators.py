"""
easy-thumbnails contrib module. Since thumbnail generation in easy-thumbnails
goes through source generators, we should make a new source generator for the
thumbnail generation, which will replace broken thumbnails with dummy ones.
In settings we set patched source generator in ``THUMBNAIL_SOURCE_GENERATORS``
setting.

- dummy_thumbnail: Dummy thumbnails generator for easy-thumbnails.
"""

import os

from django.conf import settings as django_settings

from easy_thumbnails.utils import exif_orientation as utils_exif_orientation

from six import BytesIO

from ....base import get_random_image

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.contrib.thumbnailers.easy_thumbnails.' \
            'source_generators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'dummy_thumbnail',
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
    media_root = os.path.abspath(django_settings.MEDIA_ROOT)

    if not (source and (os.path.exists(source.path)
                        or os.path.isfile(source.path))):
        random_image = get_random_image()
        random_file = open(random_image)
        from easy_thumbnails.files import ThumbnailFile

        source = ThumbnailFile(random_file.name, random_file)
        # source._set_file(random_file)
        source.name = source.file.name.replace(media_root, '')[1:]

    buf = BytesIO(source.read())

    image = Image.open(buf)
    # Fully load the image now to catch any problems with the image contents.
    try:
        # An "Image file truncated" exception can occur for some images that
        # are still mostly valid -- we'll swallow the exception.
        image.load()
    except IOError:
        pass
    # Try a second time to catch any other potential exceptions.
    image.load()

    if exif_orientation:
        image = utils_exif_orientation(image)
    return image
