from django.db import models
from django.contrib.auth import get_user_model

from .categories_dict import *

class Product(models.Model):
    title = models.CharField(max_length=120)
    about_product = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=30, choices=categories_subcategories.keys())
    subcategory = models.CharField(max_length=60, choices=subcatigories)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


