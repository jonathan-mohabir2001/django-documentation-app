from django.shortcuts import render

from django.http import HttpResponse
# Necessary package for getting views to render responses=


def index(request):
    return HttpResponse("hello, this is the polls index page")