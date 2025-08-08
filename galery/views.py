from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'galery/index.html') #primeiro parâmetro é o request, segundo é o template que será renderizado

 