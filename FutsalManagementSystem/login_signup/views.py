from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def view_signup(request):
    if request.method =="GET":
        return render(request,'signup.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['pwd'],email=request.POST['email'])
        user.save()
        return HttpResponse("Signup Successful")

def view_login_user(request):
    if request.method =="GET":
        return render (request,'login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['pwd'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"welcome.html")
        else:
            return HttpResponse("Authentication Failed")