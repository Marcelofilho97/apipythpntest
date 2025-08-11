from rest_framework import serializers
from galery.models import GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__' # Inclui todos os campos do modelo GalleryImage
        
        