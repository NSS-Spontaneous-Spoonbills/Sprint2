from django import forms
from WorkforceManagement.models import Computer


class Computer_New_Form(forms.ModelForm):
    """Form to create a new computer
    Author: Erin Meaker
    """
    class Meta:
        model = Computer
        fields = ('purchase_date', 'manufacturer', 'make')


class Computer_Update_Form(forms.ModelForm):
    """Form for updating an existing computer
    Author: Erin Meaker
    """
    class Meta:
        model = Computer
        fields = ('decom_date', 'manufacturer', 'make')




