from django.db import models


class Computer(models.Model):
    """models data for bangazon employee computers
    Author: Erin Meaker
    """
    purchase_date = models.DateTimeField()
    decom_date = models.DateTimeField()
    manufacturer = models.CharField(max_length=50)
    make = models.CharField(max_length=50)

    def __str__(self):
        return f"ComputerNum {self.id}"
