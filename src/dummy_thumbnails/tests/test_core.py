# -*- coding: utf-8 -*-
"""
Test the core package.

- DummyThumbnailsCoreTest: Test core functionality.
"""

import unittest

from bs4 import BeautifulSoup

from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from ..base import get_random_image
from ..conf import get_setting
from ..helpers import prepare_dirs_and_symlinks

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
        prepare_dirs_and_symlinks(create_dirs=True)

    @log_info
    def test_01_get_random_image(self):
        """Test ``get_random_image``."""
        image = get_random_image()
        self.assertIsNotNone(image)

    def __test_images(self, url):
        """Test if images are not empty."""
        response = self.client.get(url)
        response_content = getattr(response, 'content', "")
        soup = BeautifulSoup(response_content, "html.parser")
        images = soup.find_all(
            'img',
            attrs={'class': 'thumbnail'}
        )
        self.assertTrue(
            len(images) > 0, "Number of images should be greater that 0."
        )
        for image in images:
            source = image.get('src')
            self.assertIsNotNone(source)

    @log_info
    def test_02_test_settings(self):
        """Test settings."""
        images_path = get_setting('IMAGES_PATH')
        self.assertIsNotNone(images_path)
        default_images_path = '/path/to/images/'
        images_path_default = get_setting('I_DONT_EXIST', default_images_path)
        self.assertEqual(images_path_default, default_images_path)

    @log_info
    def test_03_test_django_imagekit(self):
        """Test ``django-imagekit``."""
        return self.__test_images(reverse('django-imagekit'))

    @log_info
    def test_04_test_sorl_thumbnail(self):
        """Test ``sorl.thumbnail``."""
        return self.__test_images(reverse('sorl-thumbnail'))

    @log_info
    def test_05_test_easy_thumbnails(self):
        """Test ``easy_thumbnails``."""
        return self.__test_images(reverse('easy-thumbnails'))


if __name__ == '__main__':
    unittest.main()
