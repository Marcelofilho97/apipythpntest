from django.shortcuts import render
from django.http import JsonResponse

def galeryimg(request):
  if request.method == 'GET':
    galeryimg = {
      'id': 1,
      'image': 'assets/images/img01.jpeg',
      'title': 'Imagem 01',
      } # os dados que serão retornados em formato JSON
    return JsonResponse(galeryimg, safe=False)
# Create your views here.

def index(request):
  galeryimg = [
    {'image': 'assets/images/img01.jpeg'},
  ]
  
  return render(request, 'galery/index.html') #primeiro parâmetro é o request, segundo é o template que será renderizado

 