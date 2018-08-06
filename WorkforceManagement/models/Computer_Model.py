from django.db import models


class Computer(models.Model):
    """models data for bangazon employee computers"""
    id = models.AutoField(primary=True)
    purchase_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    decom_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    manufacturer = models.CharField(max_length=50)
    make = models.CharField(max_length=50)