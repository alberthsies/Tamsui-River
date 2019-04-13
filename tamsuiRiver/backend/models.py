

from django.db import models

# Create your models here.

class Request(models.Model):
    company = models.TextField(default="HKUST")
    item = models.TextField(default="egg")
    price = models.IntegerField(default=2)
    quantity = models.IntegerField(default=1000)
    farmer = models.TextField(default="Albert-Emily-")

    class Meta:
        db_table = "request"



class Company(models.Model):
    name = models.TextField(default="HKUST")
    email = models.TextField(default="hkust@connect.ust.hk")

    class Meta:
        db_table = "company"

class Farmer(models.Model):
    name = models.TextField(default="Albert")
    email = models.TextField(default="albert@connect.us.hk")
    password = models.IntegerField(default="123456")
    product = models.TextField(default="egg")
    origin = models.TextField(default="Taipei City")
    certificate = models.TextField(default="SGS")
    description = models.TextField(default="We have the best eggs")

    class Meta:
        db_table = "farmer"
