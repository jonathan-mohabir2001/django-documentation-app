from django.shortcuts import render

from django.http import HttpResponse
# Necessary package for getting views to render responses=


def index(request):
    return HttpResponse("<h2>hello, this is the polls index page <h2>")
  
  
  
def about(request):

    return HttpResponse("<h2>Hello this is the about page <h2> ")
  

  

