from django.db import models

# Create your models here.
# Example model for a gallery image, ara será utilizado para armazenar informações sobre as imagens da galeria

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)  # Título da imagem, campo de texto com tamanho máximo de 100 caracteres
    image = models.ImageField(upload_to='images/')  # Campo para armazenar a imagem

    def __str__(self):
        return self.title  # Retorna o título da imagem quando o objeto é convertido para string
