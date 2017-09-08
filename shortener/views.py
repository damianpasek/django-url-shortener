from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ShortUrl


class UrlRedirectView(View):
    def get(self, request, slug):
        obj = get_object_or_404(ShortUrl, code__exact=slug)
        return HttpResponseRedirect(obj.url)
