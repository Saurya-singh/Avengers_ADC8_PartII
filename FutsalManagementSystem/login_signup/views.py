from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden
from django.template import Template,Context
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def get_isauthenticated_welcome(request):
    if request.user.is_authenticated:
        return render(request,"welcome.html")
    else:
        return redirect('login')

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

def view_logout(request):
    if(not request.user.is_authenticated):
        return HttpResponseForbidden("Please Login Again..")
    logout(request)
    return redirect('login')
