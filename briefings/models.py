from django.db import models


class Briefing(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    retailer = models.CharField(max_length=255)
    responsible = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    available = models.IntegerField()

    def __str__(self):
        return self.name
