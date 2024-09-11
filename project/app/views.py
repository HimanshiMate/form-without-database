from django.shortcuts import render
from .forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')


def regi(request):
    form=Registration()
    if request.method=='POST':
        data=Registration(request.POST)
        if data.is_valid():
            Name=data.cleaned_data['stu_name']
            Email=data.cleaned_data['stu_email']
            Contact=data.cleaned_data['stu_contact']
            # print(Name,Email,Contact)
            # data.save()
            response=render(request,'regi.html')
            response.set_cookie('name',Name)
            response.set_cookie('email',Email)
            response.set_cookie('contact',Contact)
            return response    
    return render(request,'regi.html',{'form':form})


def login(request):
    form=Login()
    if request.method=='POST':
        data=Login(request.POST)
        if data.is_valid():
            Email=data.cleaned_data['stu_email']
            Contact=data.cleaned_data['stu_contact']
            # print(Email,Contact)
            # data.save()
            # data.set_cookie('name')
            # data.set_cookie('email')
            # data.set_cookie('contact')
    return render(request,'login.html',{'form':form})


# def set(request):
#     response=render(request,'regi.html')
#     response.set_cookie('name')
#     response.set_cookie('email')
#     response.set_cookie('contact')
#     return response