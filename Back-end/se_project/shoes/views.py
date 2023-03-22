from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .form import *
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
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
            return redirect('login')
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
    total_price = 0
    context = {
        'shoes': Shoe.objects.all(),
        'cart_items': User_Order.objects.filter(owner_id=request.user.id),
    }
    for i in context['cart_items']:
        temp = ''
        for j in i.price:
            if j.isnumeric():
                temp += j
        total_price += int(temp)
    total_items = context['cart_items'].count()
    context['no_items'] = total_items
    context['total_price'] = total_price
    context['price_with_shipping'] = total_price + 40

    return render(request, 'shoes/shoppingcart.html', context)


# def recipe_delete_view(request, id=None):
#     try:
#         obj = User_Order.objects.get(id=id, user=request.user)
#     except:
#         obj = None
#     if obj is None:
#         if request.htmx:
#             return HttpResponse("Not Found")
#         raise Http404
#     if request.method == "POST":
#         obj.delete()
#         success_url = reverse('cart:list')
#         if request.htmx:
#             headers = {
#                 'HX-Redirect': success_url
#             }
#             return HttpResponse("Success", headers=headers)
#         return redirect(success_url)
#     context = {
#         "object": obj
#     }
#     return render(request, "shoes/delete.html", context)
