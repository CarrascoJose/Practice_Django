from django.db import models

# Create your models here.

class Days(models.Model):
    day = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.TextField()