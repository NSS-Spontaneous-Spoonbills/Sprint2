from django.db import models

class Training_Prog(models.Model):
    """
    Model for Training Table contains training_name, training_desc(ription), start_date
    end_date, max_attendance.
    """
    prog_name = models.CharField(max_length=50)
    training_desc = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=False)
    max_attendance = models.CharField(max_length=50)

    def __str__(self):

        return f'{self.prog_name}'