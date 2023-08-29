from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

