# -*- coding: utf-8 -*-

import os
import unittest

from bs4 import BeautifulSoup

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from ..base import get_random_image

from .base import log_info
from .helpers import setup_app

__title__ = 'dummy_thumbnails.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DummyThumbnailsCoreTest',)


class DummyThumbnailsCoreTest(TestCase):
    """Testing `django-dummy-thumbnails` core functionality."""

    def setUp(self):
        """Set up."""
        setup_app()
        self.client = Client()
        self.__prepare_dirs_and_symlinks()

    def __prepare_dirs_and_symlinks(self):
        """Prepare dirs and symlinks."""
        # What we shall do is to create dirs and make a symbolic link.
        __dirs = (
            os.path.join('examples', 'db'),
            os.path.join('examples', 'logs'),
            os.path.join('examples', 'tmp'),
            os.path.join('examples', 'media', 'static'),
            os.path.join('examples', 'static')
        )
        for __dir in __dirs:
            try:
                os.makedirs(os.path.abspath(__dir))
            except OSError:
                pass

        try:
            os.symlink(
                os.path.abspath(os.path.join('src', 'dummy_thumbnails',
                                             'static', 'dummy_thumbnails',
                                             'images', 'mixed')),
                os.path.abspath(os.path.join('examples', 'media', 'mixed'))
            )
        except OSError:
            pass

    @log_info
    def test_get_random_image(self):
        """Test ``get_random_image``."""
        image = get_random_image()
        self.assertIsNotNone(image)

    def __test_images(self, url):
        """Test if images are not empty."""
        response = self.client.get(url)
        soup = BeautifulSoup(response.content)
        images = soup.find_all(
            'img',
            attrs={'class': 'thumbnail'}
        )
        for image in images:
            source = image.get('src')
            self.assertIsNotNone(source)

    @log_info
    def test_02_test_easy_thumbnails(self):
        """Test ``easy_thumbnails``."""
        return self.__test_images(reverse('easy-thumbnails'))

    @log_info
    def test_03_test_sorl_thumbnail(self):
        """Test ``sorl.thumbnail``."""
        return self.__test_images(reverse('sorl-thumbnail'))


if __name__ == '__main__':
    unittest.main()
