from django.shortcuts import render
from django.http import HttpResponse
from coreApp.models import Glyph

def index(request):
    return render(request, 'index.html')

def glifi(request):
    GLYPHS = Glyph.objects.all()
    context = {
        'GLYPHS': GLYPHS,
    }

    return render(request, 'glifi.html', context)

def collabora(request):
    return render(request, 'collabora.html')

def community(request):
    return render(request, 'community.html')

def licenza(request):
    return render(request, 'licenza.html')

def progetto(request):
    return render(request, 'progetto.html')