from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

__all__ = ('urlpatterns',)

admin.autodiscover()

urlpatterns = []

urlpatterns_args = [
    url(r'^admin/', include(admin.site.urls)),

    # foo URLs:
    # url(r'^foo/', include('dummy_thumbnails.tests.foo.urls')),

    url(r'^$', TemplateView.as_view(template_name='home/base.html')),
    url(r'^easy-thumbnails/$',
        TemplateView.as_view(template_name='home/easy_thumbnails.html'),
        name='easy-thumbnails'),
    url(r'^sorl-thumbnail/$',
        TemplateView.as_view(template_name='home/sorl_thumbnail.html'),
        name='sorl-thumbnail'),
]

urlpatterns += i18n_patterns(*urlpatterns_args)

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    # if settings.DEBUG_TOOLBAR:
    #     import debug_toolbar
    #
    #     urlpatterns += [
    #         url(r'^__debug__/', include(debug_toolbar.urls)),
    #     ]
