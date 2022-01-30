from django.contrib import admin

from projects.models import Project, Bug

# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)
