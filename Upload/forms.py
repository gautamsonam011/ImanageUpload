from django import forms
from . import models
# class DoctorForm(forms.ModelForm): 
#     class Meta:
#         model = models.doctor_details
#         status = True
#         fields = ['doctorName',
#                 'degree', 'mobile', 'weekday',
#                 'hospitalName', 'address',
#                 'age','image',
#                 'gender','no_of_patient',
#                 'brief','email','time_in',
#                 'time_out','experience',
#                 'status','specialist']
       

  
class StudentForm(forms.ModelForm):
  
    class Meta:
        model = models.Student
        fields = ['name', 'avatar']