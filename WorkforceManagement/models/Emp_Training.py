from django.db import models

class Emp_Training(models.Model):
    """
    Model for employee_training joining table contains employee_id & and training_id
    """
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)