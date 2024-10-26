
from django.contrib import admin
from .models import Project, BlogPost

# Register the models in the admin panel
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('title', 'description','content', 'background_image')

admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost)
