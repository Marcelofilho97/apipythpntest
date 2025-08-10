from django.shortcuts import render

# Create your views here.

def index(request):
  galeryimg = [
    {'image': 'assets/images/img01.jpeg'},
  ]
  
  return render(request, 'galery/index.html') #primeiro parâmetro é o request, segundo é o template que será renderizado

 