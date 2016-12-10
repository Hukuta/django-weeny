# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django_weeny.views import URLCreateView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # The difference between $ and \Z is that $ also
    # matches just before the last newline character in a string,
    # and \Z only matches the exact end of the string
    url(r'^\Z', URLCreateView.as_view(), name='home'),

    url(r'^', include("weeny.urls")),
]

if settings.DEBUG is True:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
