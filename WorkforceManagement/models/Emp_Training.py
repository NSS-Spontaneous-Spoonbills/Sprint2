from django.db import models

class Emp_Training(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)