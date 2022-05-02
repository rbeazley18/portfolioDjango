from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'order')
    search_fields = ('title', 'description')

admin.site.register(Projects, ProjectsAdmin)