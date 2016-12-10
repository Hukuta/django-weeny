# Create your views here.

from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView

from weeny.forms import CreateURLForm
from weeny.models import WeenyURL


class URLCreateView(CreateView):
    """
    Redirects the user to the target URL.
    """
    model = WeenyURL
    form_class = CreateURLForm
    template_name = 'weeny/create_url.html'

    def form_valid(self, form):
        self.object = form.save()
        short = self.request.build_absolute_uri(str(self.object.get_absolute_url()))
        return render(self.request, self.template_name, dict(object=self.object, short=short))
