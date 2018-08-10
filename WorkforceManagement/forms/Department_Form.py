from django import forms
from WorkforceManagement.models import Department


class Department_New_Form(forms.ModelForm):
    """Form to create a new department

    Author: David Paul
    """
    class Meta:
        model = Department
        fields = ('dept_name', 'budget')
