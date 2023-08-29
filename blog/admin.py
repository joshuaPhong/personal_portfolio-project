from django.contrib import admin
# importing our project class
from .models import BlogModel
# Register your models here.
# registering our Projects admin
admin.site.register(BlogModel)