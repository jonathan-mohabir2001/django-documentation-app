from django.contrib import admin

# Register your models here

from .models import Question 

#THIS IS HOW MODELS ARE REGISTERED
admin.site.register(Question)
