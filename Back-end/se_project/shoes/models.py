from django.db import models
from django.contrib import admin
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, default="Nike")
    price = models.CharField(max_length=10, default="EGP 50")
    size = models.CharField(max_length=50, default="38 - 45")
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
    selected_size = models.CharField(max_length=10, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    order_num = models.CharField(max_length=20, default="#000000")

    def __str__(self):
        return str("In Cart Product: {x}".format(x=self.product.name))


class Orders(models.Model):
    user_ordered = models.CharField(max_length=50, default="")
    order_no = models.CharField(max_length=20, default="#000000")
    items = models.TextField(max_length=1000, default="")
    total_price = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.order_no)


class Profile(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users.username)
