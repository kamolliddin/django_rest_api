from django.db import models
from django.conf import settings
from django.core import validators
# Create your models here.


class ProductItem(models.Model):
    name = models.CharField(max_length=200)
    title = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='documents/')
    date_added = models.DateTimeField(auto_now_add=True)


class UserAccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
