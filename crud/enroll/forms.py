from django import forms
from enroll.models import userProfile

class EmployeeRegistration(forms.ModelForm):
    
    class Meta:
          model = userProfile
          fields = ['name','email','password']
          widgets={
               'name': forms.TextInput(attrs={'class':'form-control'}),

               'email': forms.TextInput(attrs={'class':'form-control'}),

               'password': forms.PasswordInput(attrs={'class':'form-control'})
          }
