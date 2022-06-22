from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import FundraiserForm
# Create your views here.

# @login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ('/')
    return render(request,'registration/login.html')

def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('/register')
        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1,
        ) 
        new_user.save() 
        return render (request,'registration/login.html')
    return render(request,'registration/register.html')

# def start_fundraiser(request):
#     if request.method == 'POST':
#         form = FundraiserForm(request.POST, request.FILES)
#         if form.is_valid():
#             fundraiser = form.save(commit=False)
#             fundraiser.admin = request.user.profile
#             fundraiser.save()
#             return redirect('neighbourhoods')
#     else:
#         form = FundraiserForm()
#     return render(request, 'neighbourhoods/create_neighbourhood.html', {'form':form})

def start_fundraiser(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = FundraiserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FundraiserForm(instance=request.user.profile)
    return render(request, 'fundraiser.html', {'form': form})
