"""
Base tests module.

- Command: Management command. Prepare the dirs and create symlinks for
  testing purposes.
"""

from django.core.management.base import BaseCommand

from ...helpers import prepare_dirs_and_symlinks

__title__ = 'dummy_thumbnails.management.commands.' \
            'dummy_thumbnails_symlink_dummy_images'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Prepare dirs and symlinks."""

    def handle(self, *args, **options):
        """Prepare dirs and symlinks."""
        prepare_dirs_and_symlinks()
