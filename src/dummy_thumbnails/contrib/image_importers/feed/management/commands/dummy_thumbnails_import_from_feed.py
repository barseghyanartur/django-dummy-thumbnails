"""
Management command for importing dummy images from feed.

- Command: Management command. Import dummy images from feed.
"""
from __future__ import print_function

from django.core.management.base import BaseCommand

from ......base import ABSOLUTE_IMAGES_PATH

from ...reader import save_feed_images
from ...settings import DEFAULT_FEED_URL

__title__ = 'dummy_thumbnails.contrib.image_importers.feed.management.' \
            'commands.dummy_thumbnails_import_from_feed'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Import dummy images from feed."""

    help = "Import dummy images from feed"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.url = None
        self.limit = None
        self.target_dir = None

    def add_arguments(self, parser):
        """Command options."""
        parser.add_argument(
            'url', nargs='?',
            default=DEFAULT_FEED_URL,
            help='URL of the feed.'
        )
        parser.add_argument(
            '--limit',
            action='store',
            dest='limit',
            default=50,
            help="Number of images to download."
        )
        parser.add_argument(
            '--target',
            action='store',
            dest='target_dir',
            default=ABSOLUTE_IMAGES_PATH,
            help="Target directory."
        )

    def set_options(self, **options):
        """Set instance variables based on an options dict."""
        self.url = options['url']
        self.limit = options['limit']
        self.target_dir = options['target_dir']

    def handle(self, *args, **options):
        """Handle."""
        self.set_options(**options)

        message = ['\n']

        saved_images = save_feed_images(self.url, self.limit, self.target_dir)

        if len(saved_images):
            message.append(
                "Images imported. The full list of imported"
                "dummy images follows.\n\n"
            )

            for saved_image in saved_images:
                message.append("{0}\n".format(saved_image))
            print(''.join(message))
