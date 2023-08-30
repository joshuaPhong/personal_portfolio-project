from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        """
        This will show the title in the admin. Instead of showing object 1...n
        """
        return self.title

