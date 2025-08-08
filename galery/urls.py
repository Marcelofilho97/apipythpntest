from django.urls import path
from galery.views import index  # Importa a view index do app galery

urlpatterns = [
    path('', index),  # endereço raiz do site, chama a view index do app galery 
]


