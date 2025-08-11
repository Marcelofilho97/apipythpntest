from django.contrib import admin
from galery.models import GalleryImage  

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title','legend','image')  # Campos a serem exibidos na lista de imagens referentes aos dados do modelo GalleryImage
    list_display_links = ('image',)  # Campos que serão links para a página de edição do objeto
    listper_page = 4  # Número de imagens por página na lista
    search_fields = ('title',)  # Campo de busca para o título da imagem  
    
    
admin.site.register(GalleryImage, GalleryImageAdmin)  # Registra o modelo no admin do Django
