import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import TemplateView
from .models import *
from .forms import FundraiserForm, DonationForm
import stripe
from django.views import View
from django.core.exceptions import ObjectDoesNotExist




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


def about(request):
    context = {}
    return render(request, 'about.html', context)

# def start_fundraiser(request, username):
#     user = User.objects.get(username=username)
#     if request.method == 'POST':
#         form = FundraiserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = FundraiserForm(instance=request.user.profile)
#     return render(request, 'fundraiser.html', {'form': form})
@login_required(login_url='/login/')
def start_fundraiser(request):
    if request.method == 'POST':
        form = FundraiserForm(request.POST, request.FILES)
        if form.is_valid():
            fundraise = form.save(commit=False)
            fundraise.admin = request.user.profile
            fundraise.save()
            return redirect('home')
    else:
        form = FundraiserForm()
    return render(request, 'fundraiser.html', {'form': form})

def all_fundraisers(request):
    all_funds = Fundraiser.objects.all()
    all_funds = all_funds[::-1]
    params = {
        'all_funds': all_funds,
    }
    return render(request, 'all_fundraisers.html', params)


def success(request):
    return render(request, 'success.html')


def single_fundraise(request, fundraise_id):
    fundraise = Fundraiser.objects.get(id=fundraise_id)
    donation = Donate.objects.filter(fundraise=fundraise)
    donation = donation[::-1]
    params = {
        'donation': donation,
        'fundraise': fundraise
    }
    return render(request, 'single_hood.html', params)


# def hood_members(request, hood_id):
#     hood = NeighbourHood.objects.get(id=hood_id)
#     members = Profile.objects.filter(neighbourhood=hood)
#     return render(request, 'hoodapp/neibas.html', {'members': members})


def donate(request, fundraise_id):
    fundraise = Fundraiser.objects.get(id=fundraise_id)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.fundraise = fundraise
            donation.save()
            return redirect('success', fundraise.id)
    else:
        form = DonationForm()
    return render(request, 'donation.html', {'form': form})


# def paypal(request):
#     ctx = {}
#     return render(request, 'valapp/paypal.html', ctx)

def paypal(request):
    return render(request, 'paypal.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")