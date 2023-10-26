from django.shortcuts import render
from django.http import HttpResponse
from coreApp.models import Glyph
from coreApp.form import GlyphFilterForm

def index(request):
    return render(request, 'index.html')

def glifi(request):
    GLYPHS = Glyph.objects.all().order_by('parola')

    if request.method == "GET":
        form = GlyphFilterForm(request.GET)
        if form.is_valid():
            query_search = form.cleaned_data.get('search')
            if query_search:
                GLYPHS = GLYPHS.filter(parola__icontains = query_search)
                
            query_categorieSemantiche = form.cleaned_data["categorieSemantiche"]            
            if query_categorieSemantiche:
                GLYPHS = GLYPHS.filter(categoria_semantica__in=query_categorieSemantiche)
            
            query_funzioniGrammaticali = form.cleaned_data["funzioniGrammaticali"]
            if query_funzioniGrammaticali:
                GLYPHS = GLYPHS.filter(funzione_grammaticale__in=query_funzioniGrammaticali)


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