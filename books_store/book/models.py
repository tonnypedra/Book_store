from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    image = models.ImageField(default="default.jpeg", upload_to='book_images')


class Product(models.Model):
    title = models.CharField(max_length=225)
    actions = models.CharField(max_length=225)
    image = models.ImageField(default="default.", upload_to='book_images')