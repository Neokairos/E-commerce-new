from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    description = models.TextField(default="nigga be empty")
    image = models.ImageField(upload_to='images/')
    rating = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)


