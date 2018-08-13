from django.views.generic import ListView, DetailView, FormView
from WorkforceManagement.models import Department, Computer, Employee
from WorkforceManagement.forms import Employee_New_Form


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

class Employee_Form_View(FormView):
    """
    Employee_Form_View inherits FormView and is using template Employee_Form.html. Ths renders a 'new' form view that admin can create a new employee with. form_class is inheriting the actual form that is going to include the necessary fields that receive the proper format.
    Includes dropdowns for department and computer.
    Built-in form_valid:
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
    Author: Jacob Smith

    """
    template_name = 'WorkforceManagement/Employee_Form.html'
    form_class= Employee_New_Form
    # NOTE! Be sure to put the slash in front of the url to route properly
    success_url = '/WorkforceManagement/employees/'

    def form_valid(self, form):

        form.save()
        return super(Employee_Form_View, self).form_valid(form)

# class Empl

