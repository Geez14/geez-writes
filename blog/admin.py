from django.contrib import admin
from .models import BlogPost

# this will allow to access the entries from admin area
admin.site.register(BlogPost)

