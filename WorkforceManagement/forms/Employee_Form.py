from django import forms
from WorkforceManagement.models import Employee

class Employee_New_Form(forms.ModelForm):
    """
    Form to add a new employee to the system. Includes all fields required by the client.
    Author: Jacob Smith
    """
    class Meta:

        model = Employee
        fields = ('name', 'start_date', 'department', 'computer' )
