from django import forms
from WorkforceManagement.models import Employee, Department

class Employee_New_Form(forms.ModelForm):
    """
    Form to add a new employee to the system
    Author: Jacob Smith
    """
    class Meta:

        # departments = forms.ModelChoiceField(queryset=Department.objects.all())

        model = Employee
        fields = ('name', 'start_date', 'department', 'computer' )