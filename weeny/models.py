# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.contrib.sites.models import Site
from django.db import IntegrityError, models
from django.contrib.contenttypes.models import ContentType

from django.utils.translation import ugettext_lazy as _


class WeenyURL(models.Model):
    url = models.CharField(max_length=255, verbose_name=_("URL"))
    slug = models.SlugField(max_length=10, db_index=True, blank=True,
                            verbose_name=_("URL code"), unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name=_("Created"))

    class Meta:
        verbose_name = _("URL")
        verbose_name_plural = _("URLs")

    def __str__(self):
        return "{code}".format(code=self.slug)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse_lazy
        return reverse_lazy("weeny_urlredirect", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:

            # check for existing short link
            old = WeenyURL.objects.filter(url=self.url).first()
            if old:
                # copy data
                self.id = old.id
                self.slug = old.slug
                self.created = old.created
                return

            # Create random slug
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            i = 1
            while i < 30:
                # Slug size is depending from number of iterations
                self.slug = get_random_string(length=min(i, 9) + 1, allowed_chars=chars)
                try:
                    super(WeenyURL, self).save(*args, **kwargs)
                    # Have unique slug
                    return
                except IntegrityError:
                    # Try another iteration
                    i += 1
            raise IntegrityError('Too many iterations while generating unique slug.')
        super(WeenyURL, self).save(*args, **kwargs)
