from django.http import request
from .forms import EditUserProfileForm, EditAdminProfileForm
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
        else:
            fm = EditUserProfileForm(instance=request.user)
            users = None
        return render(request,"home.html", {'name': request.user , "form":fm, "users":users})
    else:
        return HttpResponseRedirect('/login/')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Succesfully !!")
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/home/')

def userdetail(request, id):
    if request.user.is_authenticated:
        p = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=p)
        return render(request,"userdetail.html",{'form':fm})
    else:
        return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

    
