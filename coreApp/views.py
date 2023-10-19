from django.shortcuts import render
from django.http import HttpResponse
from coreApp.models import Glyph
from coreApp.form import GlyphFilterForm

def index(request):
    return render(request, 'index.html')

def glifi(request):
    GLYPHS = Glyph.objects.all()

    if request.method == "GET":
        form = GlyphFilterForm(request.GET)
        if form.is_valid():
            tags = form.cleaned_data["tags"]
            if tags:
                GLYPHS = GLYPHS.filter(funzione_grammaticale__in=tags)
            print(tags) 

    context = {
        'GLYPHS': GLYPHS,
        'FORM': form,
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