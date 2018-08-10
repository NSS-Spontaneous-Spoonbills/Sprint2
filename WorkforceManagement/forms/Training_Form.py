from django import forms
from WorkforceManagement.models import Training_Prog

class Training_Form(forms.ModelForm):

  class Meta:
      model = Training_Prog
      fields = ('prog_name', 'training_desc', 'start_date', 'end_date', 'max_attendance')


