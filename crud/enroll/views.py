from django.shortcuts import render
from .forms import EmployeeRegistration
from .models import userProfile
from django.http import HttpResponseRedirect
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        print(request.POST,"request")
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = EmployeeRegistration() 
    else:
        fm = EmployeeRegistration()
    userData= userProfile.objects.all()
    return render(request,'enroll/addandshow.html',{'from':fm,'userData':userData})



def update_data(request,id):
    if request.method=='POST':
        pi = userProfile.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
     pi = userProfile.objects.get(pk=id)
     fm = EmployeeRegistration(instance=pi) 
    return render(request, 'enroll/update.html',{'form':fm})


def delete(request,id):
    if request.method == 'POST':
        pi = userProfile.objects.get(id=id)
        pi.delete()
    return HttpResponseRedirect('/enroll')