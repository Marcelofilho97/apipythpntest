from django.urls import path
from galery.views import index  # Importa a view index do app galery
from galery.views import galeryimg # Importa a view galeryimg, que contém as img, do app galery


urlpatterns = [
    path('', index),  # endereço raiz do site, chama a view index do app galery 
]

