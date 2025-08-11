from django.db import models
# Define o modelo GalleryImage que representa uma imagem na galeria
  
class GalleryImage(models.Model):
  title = models.CharField(max_length=100, blank = False)  # Título da imagem, campo de texto com tamanho máximo de 100 caracteres
  legend = models.CharField(max_length=255, default= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vulputate efficitur dui, nec tristique erat dapibus at. Donec lacinia elit.") 
  image = models.CharField(max_length=255, default= "https://drive.google.com/file/d/1R3REelWOMfePR-PG_zFLPOS6Ytv4PabL/view?usp=drive_link")  # armazena apenas o caminho para uma imagem por link.

  def __str__(self):
    return self.title  # Retorna o título da imagem como representação do objeto


