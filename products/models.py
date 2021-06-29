from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price =models.FloatField()
    stock =models.IntegerField()
    image = models.ImageField()

class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()

