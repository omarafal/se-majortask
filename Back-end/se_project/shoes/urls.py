from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='shoes-home'),
    path('men/', views.men, name='shoes-men'),
    path('women/', views.men, name='shoes-women'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)