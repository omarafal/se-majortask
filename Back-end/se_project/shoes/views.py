import datetime
import uuid
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .form import *
from random import randint, randrange
from django.urls import reverse
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .helpers import send_forget_password_mail


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def home(request):
    for i in Shoe.objects.all():
        i.size = "38-45"
        i.save()
    x = [None for i in range(4)]
    temp = [2, 9, 17, 36]
    for i in range(4):
        x[i] = Shoe.objects.get(id=temp[i])
    context = {
        'shoes': Shoe.objects.all(),
        'home_items': x,
        'class_css': 'p-0 m-0 border-0 bd-example',
        'nav': True
    }
    return render(request, 'shoes/home.html', context)


def view_orders(request):
    context = {
        'orders': Orders.objects.all(),
        'class_css': 'p-0 m-0 border-0 bd-example',
        'nav': True
    }
    return render(request, 'shoes/orders_page.html', context)


def delete_order(request, num):
    if Orders.objects.filter(order_no=num):
        check = Orders.objects.get(order_no=num)
        check.delete()
        return redirect('/')
    return redirect('/')


def search_shoes(request):
    if not get_referer(request):
        raise Http404
    searched = request.POST['searched']
    searched = str(searched).replace(" ", "")
    searched = searched.lower()
    if searched.__contains__("nike"):
        searched = "Nike"
    elif searched.__contains__("adidas"):
        searched = "Adidas"
    elif searched.__contains__("balenciaga"):
        searched = "Balenciaga"
    elif searched.__contains__("newbalance") or searched.__contains__("new balance"):
        searched = "New Balance"
    elif searched.__contains__("converse"):
        searched = "Converse"
    # for i in range(x):
    #     if searched[i:i + 3] == "nike":
    #         searched = "Nike"
    shoes_brands = Shoe.objects.filter(brand__contains=searched)
    context = {
        'searched': searched,
        'shoes_brands': shoes_brands,
        'page_name': 'Search Results',
        'nav': True
    }
    return render(request, 'shoes/search_shoes.html', context)


def item_page(request, myid):
    if not get_referer(request):
        raise Http404
    form = Size(request.POST)
    context = {
        'shoes': Shoe.objects.filter(id=myid),
        'page_name': 'Item Page',
        'nav': True,
        'form': form
    }
    y = []
    x = []
    x = Shoe.objects.filter(name=Shoe.objects.get(id=myid).name)
    if x.count() > 1:
        context["more_items"] = x
        for i in x:
            y.append(i.id)
        context['more_items_id'] = y
    else:
        context["more_items"] = []
    return render(request, 'shoes/itempage.html', context)


def registration(request):
    if not get_referer(request):
        raise Http404
    msg = []
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "{x} is Created Successfully".format(x=username))
            return redirect('login')
        else:
            if not form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                msg.append("Password Doesn't Match :(")
            if User.objects.filter(username__contains=str(request.POST.get('username'))):
                msg.append("Username Already Exists :(")
            if str(form.cleaned_data.get('username')).isnumeric():
                msg.append("Username Must Contain Letters :(")
            if User.objects.filter(email__contains=str(request.POST.get('email'))):
                msg.append("Email Already Exists :(")
        return render(request, 'shoes/registration.html', {'form': form, 'page_name': 'Sign Up', 'errors': msg})
    else:
        form = RegistrationForm()
    return render(request, 'shoes/registration.html', {'form': form, 'page_name': 'Sign Up'})


def men(request):
    context = {
        'shoes': Shoe.objects.all(),
        'page_name': 'Men',
        'nav': True
    }
    return render(request, 'shoes/men.html', context)


def women(request):
    context = {
        'shoes': Shoe.objects.all(),
        'page_name': 'Women',
        'nav': True
    }
    return render(request, 'shoes/women.html', context)


def cart(request):
    if not get_referer(request):
        raise Http404
    total_price = 0
    context = {
        'shoes': Shoe.objects.all(),
        'cart_items': User_Order.objects.filter(owner_id=request.user.id, ordered=False),
        'page_name': 'Cart',
        'nav': False
    }
    if context['cart_items']:
        for i in context['cart_items']:
            temp = ''
            for j in i.product.price:
                if j.isnumeric():
                    temp += j
            total_price += int(temp) * i.product_qty
    total_items = context['cart_items'].count()
    context['no_items'] = int(total_items)
    context['total_price'] = total_price
    return render(request, 'shoes/shoppingcart.html', context)


def checkout(request):
    if not get_referer(request):
        raise Http404
    total_price = 0
    if User_Order.objects.filter(ordered=False, owner=request.user):
        x = randint(100000, 999999)
        for i in User_Order.objects.filter(owner=request.user, ordered=False):
            i.ordered = True
            i.created_at = datetime.datetime.now()
            i.order_num = "#{h}".format(h=x)
            i.save()
            temp_p = ''
            for j in i.product.price:
                if j.isnumeric():
                    temp_p += j
            total_price += int(temp_p) * i.product_qty
            # i.delete()
        temp = ""
        for i in User_Order.objects.filter(owner=request.user, ordered=True):
            temp += "Shoe Name: {x}\nShoe Brand: {q}\nSelected Sizes: {z}\nQuantity: {y}\n\n".format(x=i.product.name,
                                                                                                     q=i.product.brand,
                                                                                                     z=i.selected_size,
                                                                                                     y=i.product_qty)
            i.delete()
        Orders.objects.create(order_no=x, items=temp)
        other = Orders.objects.get(order_no=x)
        other.user_ordered = "{x} {y}".format(x=str(request.user.first_name), y=str(request.user.last_name))
        other.total_price = str(total_price)
        other.save()
        context = {
            'page_name': "Checkout",
            'order_no': x
        }
    else:
        context = {
            'page_name': "Checkout",
            'Error': "Stop Refreshing :("
        }
    return render(request, 'shoes/checkout.html', context)
    # messages.success(request, "Please Fill Your Cart Then Checkout :(")
    # return redirect('cart')


def add_To_Cart(request, xid):
    if not get_referer(request):
        raise Http404
    if request.POST.get("sizeselect"):
        if User_Order.objects.filter(product_id=xid, ordered=False, owner=request.user):
            check = User_Order.objects.get(product_id=xid, owner=request.user)
            check.selected_size += ", {y}".format(y=request.POST.get("sizeselect"))
            check.product_qty += 1
            check.save()
            messages.success(request, "Item Already in Cart")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        User_Order.objects.create(owner=request.user, product_id=xid, product_qty=1)
        messages.success(request, "Item Added To Cart")
        hh = User_Order.objects.get(owner=request.user, product_id=xid)
        hh.selected_size = request.POST.get("sizeselect")
        hh.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        messages.success(request, "Please Select a Size")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def remove_From_Cart(request, xid):
    if not get_referer(request):
        raise Http404
    if User_Order.objects.filter(product_id=xid, owner=request.user):
        check = User_Order.objects.get(product_id=xid, owner=request.user)
        check.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    messages.success(request, "Item Not in Cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def profile(request):
    msg = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if User.objects.filter(username=request.POST.get('username')):
            if request.user.username == request.POST.get('username'):
                pass
            else:
                messages.error(request, 'Username Already Exists :(')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if request.POST.get('first_name').isnumeric() or request.POST.get('last_name').isnumeric():
            messages.error(request, 'First/Last Name Can’t Be Entirely Numeric :(')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not request.POST.get('first_name') or not request.POST.get('last_name'):
            messages.error(request, 'Do Not Leave First/Last Name Blank :(')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            if form.is_valid():
                form.save()
            msg = 'Data has been saved'
    form = ProfileForm(instance=request.user)
    context = {
        'user': request.user,
        'class_css': 'p-0 m-0 border-0 bd-example',
        'nav': True,
        'form': form,
        'msg': msg
    }
    return render(request, 'shoes/profile.html', context)


class PasswordChange(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('login')
