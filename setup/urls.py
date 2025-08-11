from django.contrib import admin
from django.urls import path, include
from galery.views import GalleryImageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', GalleryImageViewSet, basename='Gallery')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Inclui as URLs do viewset no app galery
]
