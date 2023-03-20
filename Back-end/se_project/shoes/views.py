from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    context = {
        'shoes': Shoe.objects.all()
    }
    return render(request, 'shoes/home.html', context)


def search_shoes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        shoes_brands = Shoe.objects.filter(brand__contains=searched)
        return render(request, 'shoes/search_shoes.html', {'searched': searched, 'shoes_brands': shoes_brands})
    else:
        return render(request, 'shoes/search_shoes.html')


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account is Created Successfully")
            return redirect('sign_in')
        else:
            messages.error(request, "Password Doesn't Match :(")
    else:
        form = RegistrationForm()
    return render(request, 'shoes/registration.html', {'form': form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('shoes-home')
        else:
            messages.error(request, "Wrong Username or Password :(")
    else:
        form = AuthenticationForm()
    return render(request, 'shoes/sign_in.html', {'form': form})


def men(request):
    return render(request, 'shoes/men.html')


def women(request):
    return render(request, 'shoes/women.html')


def cart(request):
    context = {
        'shoes': Shoe.objects.all()
    }
    return render(request, 'shoes/shoppingcart.html', context)