from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='shoes-home'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('search_shoes/', views.search_shoes, name='search_shoes'),
    path('register/', views.registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shoes/sign_in.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shoes/sign_out.html'), name='logout'),
    path('cart/', views.cart, name='cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
