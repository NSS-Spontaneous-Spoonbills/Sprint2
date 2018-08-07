from django.views.generic import ListView
from WorkforceManagement.models import Department, Computer, Employee


class Employee_List_View(ListView):
    model = Employee
    context_object_name = 'Employee_List'