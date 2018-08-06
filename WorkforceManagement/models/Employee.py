from django.db import models

class Employee(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    computer_id = models.ForeignKey(Computer. on_delete=models.CASCADE)
    is_supervisor = models.BooleanField(default=False)
    name = models.CharField(max_length="50")
    start_date = models.DateField(auto_now_add=True)