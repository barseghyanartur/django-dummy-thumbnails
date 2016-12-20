from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from nine import versions

__all__ = ('urlpatterns',)

admin.autodiscover()

urlpatterns = []

if versions.DJANGO_GTE_1_9:
    SORL_THUMBNAIL_TEMPLATE = 'home/sorl_thumbnail.html'
    EASY_THUMBNAILS_TEMPLATE = 'home/easy_thumbnails.html'
else:
    SORL_THUMBNAIL_TEMPLATE = 'home/sorl_thumbnail_django_1_8.html'
    EASY_THUMBNAILS_TEMPLATE = 'home/easy_thumbnails_django_1_8.html'

urlpatterns_args = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='home/base_site.html')),
    url(r'^django-imagekit/$',
        TemplateView.as_view(template_name='home/django_imagekit.html'),
        name='django-imagekit'),
    url(r'^sorl-thumbnail/$',
        TemplateView.as_view(template_name=SORL_THUMBNAIL_TEMPLATE),
        name='sorl-thumbnail'),
    url(r'^easy-thumbnails/$',
        TemplateView.as_view(template_name=EASY_THUMBNAILS_TEMPLATE),
        name='easy-thumbnails'),
]

urlpatterns += i18n_patterns(*urlpatterns_args)

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    if settings.DEBUG_TOOLBAR:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
