# main entry urls.py configuration py file

from django.contrib import admin
from django.urls import include, path
# let django import the necessary modules

urlpatterns = [
    path('', include('polls.urls')),
    # let django know this is using the urls from the polls application
    path('admin/', admin.site.urls),
]
