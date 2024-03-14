from django.shortcuts import render, redirect
from Upload import models, forms
from django.http import HttpResponse
# Create your views here.


def home(request):
    # form = forms.DoctorForm()
    if request.method == 'POST':
    #     form = forms.DoctorForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         doctor=forms.DoctorForm.save(commit=False)
    #         doctor=doctor.save()
    #         return redirect('/')
    # return render(request, "Upload/home.html")

        docname = request.POST.get('docname')
        docage = request.POST.get('docage')
        docgender = request.POST.get('docgender')
        docmobile = request.POST.get('docmobile')
        dochos = request.POST.get('dochos')
        docdegree = request.POST.get('docdegree')
        docaddress = request.POST.get('docaddress')
        docweek = request.POST.get('docweek')
        docexp = request.POST.get('docexp')
        docno = request.POST.get('docno')
        docbrief = request.POST.get('docbrief')
        docemail = request.POST.get('docemail')
        docspec = request.POST.get('docspec')
        doctimein = request.POST.get('doctimein')
        doctimeout = request.POST.get('doctimeout')
        docimg = request.POST.get('docimg')
       
        
        doct = models.doctor_details()
        
        doct.doctorName = docname
        doct.age = docage
        doct.gender = docgender
        doct.degree = docdegree
        doct.mobile = docmobile
        doct.weekday = docweek
        doct.hospitalName = dochos
        doct.address = docaddress
        doct.experience = docexp
        doct.image = docimg
        doct.no_of_patient = docno
        doct.brief = docbrief
        doct.email = docemail
        doct.time_in = doctimein
        doct.time_out = doctimeout
        doct.image = docimg
        doct.specialist = docspec
       
        doct.save()

        return redirect('message')
    return render(request, "Upload/home.html")

def message(request):
    return HttpResponse('Successfully')

def avatarView(request):
  
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = forms.StudentForm()
    return render(request, 'Upload/studentform.html', {'form' : form})
  
  
def uploadok(request):
    return HttpResponse(' upload successful')
