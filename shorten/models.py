from django.db import models


# Create your models here.

class URL(models.Model):
    original_url = models.URLField()
    shortened_path = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.original_url}"
