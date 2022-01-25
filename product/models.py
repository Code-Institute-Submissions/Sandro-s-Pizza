from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    """Item model class"""
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Overrides default string method"""
        return str(self.name)


class Review(models.Model):
    """Review model class"""
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        """Overrides default string method"""
        return str(self.title)
