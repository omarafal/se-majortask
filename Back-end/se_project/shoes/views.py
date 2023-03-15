from django.shortcuts import render
from .models import Shoe


def home(request):
    context = {
        'Shoes': Shoe.objects.all()
    }
    return render(request, 'shoes/home.html',context)


def search_shoes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        shoes_brands = Shoe.objects.filter(brand__contains=searched)
        return render(request, 'shoes/search_shoes.html', {'searched': searched, 'shoes_brands': shoes_brands})
    else:
        return render(request, 'shoes/search_shoes.html', {})


def men(request):
    return render(request, 'shoes/men.html')


def women(request):
    return render(request, 'shoes/women.html')
