from django.db import models
from Home.models import User

# Create your models here.


class listOfCoins(models.Model):
    coinName = models.CharField(max_length=150)
    priceUSD = models.DecimalField(max_digits=25, decimal_places=20)


class Exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exchange_name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
