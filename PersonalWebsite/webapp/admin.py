
from django.contrib import admin
from .models import Project, BlogPost

# Register the models in the admin panel
admin.site.register(Project)
admin.site.register(BlogPost)
