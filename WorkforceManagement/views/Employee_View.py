from django.views.generic import ListView, DetailView
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
    template_name = 'WorkforceManagement/Employee_List.html'

class Employee_Detail_View(DetailView):
    """
    Employee_Detail_View inherits DetailView and is using the Employee model and using the URL pk to find the specific Employee VIA id
    *context_object_name is a method override to rename from 'object_list' --> 'Employee_Detail'
    *template_name is a method that looks for an html file called 'Employee_Detail.html' to send information 
        Author: Cashew Rose

    """
    model = Employee
    context_object_name = 'Employee_Detail'
    template_name = 'WorkforceManagement/Employee_Detail.html'