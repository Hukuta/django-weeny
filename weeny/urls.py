# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url

from weeny.views import URLRedirectView


urlpatterns = [
    url(r"^(?P<slug>[a-zA-Z0-9]+)$", view=URLRedirectView.as_view(), name="weeny_urlredirect")
]
