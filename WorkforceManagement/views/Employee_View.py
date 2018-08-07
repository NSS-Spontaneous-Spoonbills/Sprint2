from django.views.generic import ListView
from WorkforceManagement.models import Department, Computer, Employee


class Employee_List_View(ListView):
    template_name = 'WorkforceManagement/employees_list.html'
    context_object_name = 'employees_list'

    def get_queryset(self):
        return Employee.objects.all()