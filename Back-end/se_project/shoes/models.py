from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Shoe(models.Model):
    brands_List = (
        ('1', 'Nike'),
        ('2', 'Adidas'),
        ('3', 'Converse'),
        ('4', 'New Balance')
    )
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, default="Nike", choices=brands_List)

    def __str__(self):
        return self.name
