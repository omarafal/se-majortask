from django.shortcuts import render
from .models import Shoe


def home(request):
    return render(request, 'shoes/home.html')


def men(request):
    return render(request, 'shoes/men.html')


def women(request):
    return render(request, 'shoes/women.html')
