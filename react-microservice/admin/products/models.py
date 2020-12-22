from django.db import models


# Create your models here.
# Product will have id and following 3 fields
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


# This table will have only id field. So pass
class User(models.Model):
    pass
