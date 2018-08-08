from django import forms
from WorkforceManagement.models import Computer


class Computer_New_Form(forms.ModelForm):
    """Form to create a new computer

    Author: Erin Meaker
    """

    model = Computer
    fields = ('purchase_date', 'decom_date', 'manufacturer', 'make')
