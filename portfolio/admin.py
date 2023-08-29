from django.contrib import admin
# importing our project class
from .models import Project
# Register your models here.
# registering our Projects admin
admin.site.register(Project)
