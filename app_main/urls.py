from django.urls import path
from .views import index, about, license

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('license/', license, name='license'),
    
]