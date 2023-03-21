from django.urls import path


from . import views
# from this directory import the views.py and all of its functions

# Access the index function of the views file
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
