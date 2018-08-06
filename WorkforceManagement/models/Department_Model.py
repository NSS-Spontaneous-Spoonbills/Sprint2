
from django.db import models


class Department(models.Model):
    """models department records for bangazon corp """
    id = models.AutoField(primary=True)
    dept_name = models.CharField(max_length=50)
    budget = models.SmallIntegerField()

    def __str__(self):

        return f'{self.dept_name}'
