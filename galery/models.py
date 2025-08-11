from django.db import models
# Define o modelo GalleryImage que representa uma imagem na galeria
  
class GalleryImage(models.Model):
  title = models.CharField(max_length=100, blank = False)  # Título da imagem, campo de texto com tamanho máximo de 100 caracteres
  legend = models.CharField(max_length=255, default= "no legend")# Legenda da imagem, campo de texto com tamanho máximo de 255 caracteres e valor padrão "no legend" 
  image = models.CharField(max_length=255)  # armazena apenas o caminho.

  def __str__(self):
    return self.title  # Retorna o título da imagem como representação do objeto
