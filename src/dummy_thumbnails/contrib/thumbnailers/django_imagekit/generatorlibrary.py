"""
django-imagekit contrib module. Since thumbnail generation in django-imagekit
goes through generators, we should make a new generator for the thumbnail
generation, which will replace broken thumbnails with dummy ones. The
default generator is being replaced (unregistered) here with patched one
``DummyThumbnail`` (registered).

- DummyThumbnail: Dummy thumbnails generator for django-imagekit.
"""

from imagekit.cachefiles import ImageCacheFile
from imagekit.processors import Thumbnail as ThumbnailProcessor
from imagekit.registry import register, unregister
from imagekit.specs import ImageSpec

from ....base import get_random_image

__title__ = 'dummy_thumbnails.contrib.thumbnailers.django_imagekit.' \
            'generatorlibrary'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DummyThumbnail',
)


class DummyThumbnail(ImageSpec):
    """Dummy thumbnail."""

    def __init__(self, width=None, height=None, anchor=None, crop=None,
                 upscale=None, **kwargs):
        self.processors = [ThumbnailProcessor(width, height, anchor=anchor,
                                              crop=crop, upscale=upscale)]

        source = kwargs.get('source')
        if not (source is not None and getattr(source, 'name', None)):
            random_image = get_random_image()
            source = ImageCacheFile(self, name=random_image)
            kwargs['source'] = source

        super(DummyThumbnail, self).__init__(**kwargs)


unregister.generator('imagekit:thumbnail')
register.generator('imagekit:thumbnail', DummyThumbnail)
