from django.contrib import admin

# Register your models here.
from gitHubRunner.models import Platform, Category, DataSource, Project

admin.site.register(Platform)
admin.site.register(Category)
admin.site.register(DataSource)
admin.site.register(Project)
