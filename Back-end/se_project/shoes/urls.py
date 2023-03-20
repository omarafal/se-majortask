from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='shoes-home'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('search_shoes/', views.search_shoes, name='search_shoes'),
    path('registration/', views.registration, name='registration'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('cart/', views.cart, name='cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
