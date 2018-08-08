from django.db import models

class Employee(models.Model):
    """
    Model for Employee Table contains department_id, computer_id, is_supervisor, name, & start_date
    """
    training = models.ManyToManyField('Training_Prog')
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE)
    is_supervisor = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):

        return f'{self.name}'

