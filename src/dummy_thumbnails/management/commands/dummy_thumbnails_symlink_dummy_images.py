"""
Management command for creating symlinks.

- Command: Management command. Prepare the dirs and create symlinks for
  testing purposes.
"""

from django.core.management.base import BaseCommand

from ...helpers import prepare_dirs_and_symlinks

__title__ = 'dummy_thumbnails.management.commands.' \
            'dummy_thumbnails_symlink_dummy_images'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Prepare dirs and symlinks."""

    help = "Prepare dirs and make symlinks to dummy images"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--create-dirs',
            action='store_true',
            dest='create_dirs',
            default=False,
            help='Create additional dirs',
        )

    def handle(self, *args, **options):
        """Handle."""
        create_dirs = options.get('create_dirs', False)
        prepare_dirs_and_symlinks(create_dirs=create_dirs)
