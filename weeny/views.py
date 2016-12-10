# Create your views here.

from __future__ import unicode_literals

from django import http
from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin

from weeny.models import WeenyURL


class URLRedirectView(SingleObjectMixin, RedirectView):
    """
    Redirects the user to the target URL.
    """
    model = WeenyURL

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(URLRedirectView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        url = self.object.url or '/'
        return http.HttpResponsePermanentRedirect(url)
