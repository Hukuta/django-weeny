# -*- coding: utf-8 -*-

from django.contrib import admin

from weeny.forms import CreateURLForm

from weeny.models import WeenyURL


@admin.register(WeenyURL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url', 'created')
    ordering = ('-id',)
    search_fields = ('slug', 'url')
    form = CreateURLForm
