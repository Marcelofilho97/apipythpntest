from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galery.urls')),  # endereço raiz do site, chama a view index do app galery
]

