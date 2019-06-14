import os

from django.conf import settings

import feedparser

from eximagination.utils import obtain_image

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.contrib.image_importers.feed.reader'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('obtain_image',)


def save_feed_images(url, limit, destination_directory):
    """Save feed images.

    :param str url:
    :param int limit:
    :param str destination_directory:
    :return list: List of strings - paths to saved images.
    """
    feed = feedparser.parse(url)
    urls = []
    for item in feed.entries:
        if len(urls) > limit:
            break
        try:
            enclosure = item.enclosures[0]
            if enclosure.type == 'image/jpeg':
                urls.append(enclosure.href)
        except (AttributeError, KeyError):
            pass

    filenames = []

    for _url in urls:
        file_data = obtain_image(
            image_source=_url,
            save_to=destination_directory,
            media_url=destination_directory,
            force_update=False,
            debug=settings.DEBUG
        )
        if file_data:
            filenames.append(os.path.join(settings.MEDIA_ROOT, file_data[0]))

    return filenames
