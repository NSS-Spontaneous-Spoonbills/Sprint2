from django import forms
from WorkforceManagement.models import Training_Prog

class Training_New_Form(forms.ModelForm):

  class Meta:
      model = Training_Prog
      fields = ('prog_name', 'training_desc', 'max_attendance')


