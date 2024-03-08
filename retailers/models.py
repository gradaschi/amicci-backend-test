from django.db import models
from vendors.models import Vendor


class Retailer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    vendors = models.ManyToManyField(Vendor)

    def __str__(self):
        return self.name
