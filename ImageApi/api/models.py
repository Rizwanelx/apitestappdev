from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    image = models.ImageField( max_length=254, blank=True, null=True)
    description = models.CharField(max_length=300, default='SOME STRING')




