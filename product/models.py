from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
