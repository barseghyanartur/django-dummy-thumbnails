"""
Management command for verifying dummy images.

- Command: Management command. Verify dummy images.
"""
from __future__ import print_function

import codecs
import os

from django.core.management.base import BaseCommand

from six import BytesIO
from six.moves import input

from ...base import ABSOLUTE_IMAGES_PATH

try:
    from PIL import Image
except ImportError:
    import Image

__title__ = 'dummy_thumbnails.management.commands.' \
            'dummy_thumbnails_verify_dummy_images'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Verify dummy images."""

    help = "Verify broken dummy images"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.interactive = None
        self.verbosity = None
        self.list_invalid_files = None

    def add_arguments(self, parser):
        """Command options."""
        parser.add_argument(
            '--noinput',
            action='store_false',
            dest='interactive',
            default=True,
            help="Do NOT prompt the user for input of any kind."
        )
        parser.add_argument(
            '--list',
            action='store_true',
            dest='list_invalid_files',
            default=False,
            help="Just list files without asking for removal."
        )

    def set_options(self, **options):
        """Set instance variables based on an options dict."""
        self.interactive = options['interactive']
        self.verbosity = options['verbosity']
        self.list_invalid_files = options['list_invalid_files']

    def handle(self, *args, **options):
        """Handle."""
        self.set_options(**options)

        message = ['\n']

        broken_images = []

        for filename in os.listdir(ABSOLUTE_IMAGES_PATH):
            abs_path = os.path.join(ABSOLUTE_IMAGES_PATH, filename)
            if os.path.isfile(abs_path):
                with codecs.open(abs_path, mode='rb') as image_file:

                    buf = BytesIO(image_file.read())

                    try:
                        image = Image.open(buf)

                        try:
                            image.verify()
                            continue
                        except Exception:
                            # We should remove the image
                            broken_images.append(abs_path)
                    except IOError:
                        # We should remove the image
                        broken_images.append(abs_path)

        if not len(broken_images):
            print("\nNo broken dummy images detected.\n")
        else:
            if self.list_invalid_files:
                message.append(
                    "Broken dummy images detected. The full list of broken "
                    "dummy images follows.\n\n"
                )
                for broken_image in broken_images:
                    message.append("{0}\n".format(broken_image))
                print(''.join(message))
            else:
                if self.interactive:
                    message.append(
                        "Broken dummy images detected. You will be now "
                        "prompted to delete them one by one. \nType 'yes' to "
                        "confirm a single image file removal and 'no' to "
                        "cancel it.\n\n"
                    )
                    for broken_image in broken_images:
                        message.append(
                            "Delete {0} file? ".format(broken_image)
                        )
                        if input(''.join(message)) == 'yes':
                            os.remove(broken_image)
                        message = []
                    print('\n')
                else:
                    message.append(
                        "Broken dummy images detected and removed. The full "
                        "list of removed broken dummy images follows.\n\n"
                    )
                    for broken_image in broken_images:
                        message.append("{0}\n".format(broken_image))
                        os.remove(broken_image)

                    print(''.join(message))
