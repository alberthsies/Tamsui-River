

from django.db import models

# Create your models here.

class Request(models.Model):
    company = models.TextField()
    item = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    farmer = models.TextField()


class Company(models.Model):
    name = models.TextField(default="HKUST")
    email = models.TextField(default="hkust@connect.ust.hk")


class Farmer(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    product = models.TextField()
    origin = models.TextField()
    certificate = models.TextField()
    description = models.TextField()