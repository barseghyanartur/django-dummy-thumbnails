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
__copyright__ = '2016-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Prepare dirs and symlinks."""

    help = "Prepare dirs and make symlinks to dummy images"

    def handle(self, *args, **options):
        """Handle."""
        prepare_dirs_and_symlinks()
