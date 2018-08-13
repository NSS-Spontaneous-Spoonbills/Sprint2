from django.db import models


class Computer(models.Model):
    """models data for bangazon employee computers
    Author: Erin Meaker
    """
    purchase_date = models.DateTimeField(null=True, blank=True)
    decom_date = models.DateTimeField(null=True, blank=True)
    manufacturer = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    has_been_assigned = models.BooleanField(default=False)

    def __str__(self):
        return f"ComputerNum {self.id}"