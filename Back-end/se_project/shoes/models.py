from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, default="Nike")
    price = models.CharField(max_length=10, default="EGP 50")
    size = models.CharField(max_length=50, default="40, 41, 42, 43, 44, 45")
    color = models.CharField(max_length=50, default="White")
    color_hexa = models.CharField(max_length=50, default="#000000")
    Type = models.CharField(max_length=10, default="Men")
    img = models.ImageField(upload_to='shoes_images')

    def __str__(self):
        return self.name


class User_Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
