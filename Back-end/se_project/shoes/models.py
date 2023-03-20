from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, default="Nike")
    price = models.CharField(max_length=10, default="EGP 50")
    sizes = models.CharField(max_length=50, default="42")
    color = models.CharField(max_length=50, default="White")
    Type = models.CharField(max_length=10, default="Men")
    img = models.ImageField(upload_to='shoes_images')

    def __str__(self):
        return self.name

