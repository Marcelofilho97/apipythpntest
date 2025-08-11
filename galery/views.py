from galery.models import GalleryImage
from galery.serializers import GalleryImageSerializer
from rest_framework import viewsets

class GalleryImageViewSet(viewsets.ModelViewSet):
  queryset = GalleryImage.objects.all()  # Obtém todas as imagens da galeria
  serializer_class = GalleryImageSerializer  # Define o serializer a ser usado
