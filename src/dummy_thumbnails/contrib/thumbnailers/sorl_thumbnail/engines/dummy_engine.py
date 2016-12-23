"""
sorl-thumbnail contrib module. Since thumbnail generation in sorl-thumbnail
goes through thumbnail engine, we should make a new thumbnail engine for the
thumbnail generation, which will replace broken thumbnails with dummy ones.
In settings we set patched thumbnail engine in ``THUMBNAIL_ENGINE``
setting.

- DummyThumbnailsEngine: Dummy thumbnails engine for sorl-thumbnail.
"""

from __future__ import absolute_import

from six import BytesIO
from sorl.thumbnail.engines.pil_engine import Engine as PILEngine
from sorl.thumbnail.images import ImageFile

from .....base import get_random_image

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.contrib.thumbnailers.sorl_thumbnail.' \
            'engines.dummy_engine'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DummyThumbnailsEngine',
)


class DummyThumbnailsEngine(PILEngine):
    """DummyThumbnailsEngine engine."""

    def get_image(self, source):
        """Get image."""
        if not (source and source.exists()):
            random_image = get_random_image()
            random_file = open(random_image)
            source = ImageFile(random_file)

        buf = BytesIO(source.read())

        image = Image.open(buf)
        # Fully load the image now to catch any problems with the image
        # contents.
        try:
            # An "Image file truncated" exception can occur for some images
            # that are still mostly valid -- we'll swallow the exception.
            image.load()
        except IOError:
            pass
        # Try a second time to catch any other potential exceptions.
        image.load()
        return image
