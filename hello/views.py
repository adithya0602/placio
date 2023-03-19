from django.contrib import messages
from django.db import models
from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib import auth
def main(request):
    return render(request,"hello/main.html")
def companyc(request):
    return render(request,"hello/companyc.html")
def contactus(request):
    return render(request,"hello/contactus.html")
def main1(request):
    return render(request,"hello/main1.html")
def index(request):
    return render(request,"hello/index.html")
def about(request):
    return render(request,"hello/about.html")
def companies_visited(request):
    return render(request,"hello/company.html")
def contact(request):
    return render(request,"hello/contact.html")
def placed(request):
    return render(request,"hello/placed.html")
def stat(request):
    return render(request,"hello/stat.html")

def register(request):
    msg=None
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            msg='user created'
            return redirect('login_view')
        else:
            msg='form is not valid'
    else:
        form=SignUpForm()
    return render(request,'hello/register.html',{'form':form,'msg':msg})


def login_view(request):
    form=LoginForm(request.POST or None)
    msg=None
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None and user.is_student:
                login(request,user)
                return redirect('main')
            elif user is not None and user.is_recruiter:
                login(request,user)
                return redirect('main1')
            else:
                msg='invalid credentials'
        else:
            msg='error validating form'
    return render(request,'hello/login.html',{'form':form,'msg':msg})

def logout_page(request):
    logout(request)
    return redirect("home")