from django.views.generic import ListView
from WorkforceManagement.models import Department, Computer, Employee


class Employee_List_View(ListView):
    """
    Employee_List_View inherits ListView and is using the Employee model
    *context_object_name is a method override to rename from 'object_list' --> 'Employee_List'
        *Looks for an html file called 'Employee_List.html' to send information
    Author: Jacob Smith

    """
    model = Employee
    context_object_name = 'Employee_List'