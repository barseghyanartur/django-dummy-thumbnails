"""
This allows usage of `easy-thumbnails` in templates
by {% load easy_thumbnail %} instead of traditional
{% load thumbnail %}. It's specifically useful in projects
that do make use of multiple thumbnailer libraries (for
instance `sorl-thumbnail` alongside `easy-thumbnails`).
"""
from __future__ import absolute_import

from easy_thumbnails.templatetags.thumbnail import *  # NOQA
