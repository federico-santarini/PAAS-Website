from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def collabora(request):
    return render(request, 'collabora.html')

def community(request):
    return render(request, 'community.html')

def glifi(request):
    return render(request, 'glifi.html')

def licenza(request):
    return render(request, 'licenza.html')

def progetto(request):
    return render(request, 'progetto.html')