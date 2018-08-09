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

    template_name = 'WorkforceManagement/Employee_Form.html'
    form_class = Employee_New_Form
    context_object_name= 'Employee_Form'
    # NOTE! Be sure to put the slash in front of the url to route properly
    success_url = '/WorkforceManagement/employees/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["location"] = "new_employee"
    #     return context


    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()
        return super(Employee_Form_View, self).form_valid(form)