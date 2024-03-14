from django.db import models

# Create your models here.


class doctor_details(models.Model):
    doctorName = models.CharField(max_length=100)
    degree = models.CharField(max_length=500, null=False, blank=False, default=False)
    mobile = models.CharField(max_length=12,default=False)
    weekday = models.CharField(max_length=500, default=False)
    hospitalName = models.CharField(max_length=500, null=False, blank=False, default=False)
    address = models.CharField(max_length=500, null=False, blank=False, default=False)
    image = models.ImageField()
    age = models.IntegerField(null=True)
    experience = models.IntegerField(default=False)
    gender = models.CharField(max_length=500, null=True)
    no_of_patient = models.IntegerField(null=True)
    brief = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True)
    time_in = models.TimeField()
    time_out = models.TimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    specialist = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.doctorName
  
class Student(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name