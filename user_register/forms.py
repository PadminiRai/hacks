from django import forms
from .models import *
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        #fields = '__all__'
        fields = ('eno','ename','position','mobile')#for specific fields
        labels = {
            'eno': 'Employee Number',
            'ename': 'Employee Name ',
            'position': 'Employee Position',
            'mobile': 'Phone Number'
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='--SELECT--'
        self.fields['position'].required=False


