from django.db import models

# Create your models here.

class Request(models.Model):
    company = models.TextField(default="HKUST")
    item = models.TextField(default="egg")
    price = models.IntegerField(default=2)
    quantity = models.IntegerField(default=1000)
    farmer = models.TextField(default="Albert-Emily-")

    class Meta:
        db_table = "music"