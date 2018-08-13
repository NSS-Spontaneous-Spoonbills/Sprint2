from django.db import models
from django.urls import reverse

class Employee(models.Model):
    """
    Model for Employee Table contains department_id, computer_id, is_supervisor, name, & start_date
    Includes one many to many field: training that removes the need for a joining table between employees and training programs
    """
    training = models.ManyToManyField('Training_Prog')
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE)
    is_supervisor = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=False)

    def get_absolute_url(self):
        return reverse('employee-new', kwargs={'pk': self.pk})

    def __str__(self):

        return f'{self.name}'

