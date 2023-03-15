from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='shoes-home'),
    path('men/', views.men, name='shoes-men'),
    path('women/', views.women, name='shoes-women'),
    path('search_shoes/', views.search_shoes, name='search_shoes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)