#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from weeny.models import WeenyURL

from django.core.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _


class CreateURLForm(ModelForm):
    class Meta:
        model = WeenyURL
        fields = ('url',)

    def clean_url(self):
        data = self.cleaned_data.get('url', '')
        if '.' not in data:
            raise ValidationError(_("Invalid URL"))
        if not (data.startswith('http://') or data.startswith('https://')):
            if '://' in data:
                raise ValidationError(_("Unsupported protocol: only http and https"))
            data = "http://" + data
        return data
