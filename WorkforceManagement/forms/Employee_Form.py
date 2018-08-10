from django import forms
from WorkforceManagement.models.Employee_Model import Employee

class Employee_New_Form(forms.ModelForm):
    """
    Form to add a new employee to the system
    Author: Jacob Smith
    """
    class Meta:

        model = Employee
        fields = ('name', 'start_date', 'department', 'computer' )

# Employee_Computer_Inline_FormSet = forms.inlineformset_factory(
#     models.Employee,
#     models.Computer,
#     fields=('computer')
# )


