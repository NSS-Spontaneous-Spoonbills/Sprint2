from django.db import models


class Computer(models.Model):
    """models data for bangazon employee computers"""
    purchase_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    decom_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    manufacturer = models.CharField(max_length=50)
    make = models.CharField(max_length=50)

    def __str__(self):
        return f"ComputerNum_something"
