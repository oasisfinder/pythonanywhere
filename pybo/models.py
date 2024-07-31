from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


