from django.contrib import admin
from .models import Project, Comment, Year

# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Year)
