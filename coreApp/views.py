from django.shortcuts import render
from django.http import HttpResponse
from coreApp.models import Glyph, SelectedImage
from coreApp.form import GlyphFilterForm
import io
import zipfile
import os

def index(request):
    return render(request, 'index.html')

def glifi(request):
    GLYPHS = Glyph.objects.all().order_by('parola')
    form = GlyphFilterForm(request.GET)

    
    if request.method == "GET":
        # form = GlyphFilterForm(request.GET)
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
    
    if request.method == "POST":
        # pass
        selected_image_ids = request.POST.getlist("selected_images")
        #print(selected_image_ids)
        # Clear previously selected images for the current user
        SelectedImage.objects.all().delete()

        # Add the newly selected images
        for image_id in selected_image_ids:
            selected_image = SelectedImage(foreignGlyph_id=image_id)
            selected_image.save()

    selected_images = SelectedImage.objects.all()

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

def download_selected_images(request):
    selected_image_ids = request.POST.getlist("selected_images")
    print(selected_image_ids)
    
    # Clear previously selected images for the current user
    SelectedImage.objects.all().delete()

    # Add the newly selected images
    for image_id in selected_image_ids:
        selected_image = SelectedImage(foreignGlyph_id=image_id)
        selected_image.save()

    selected_images = SelectedImage.objects.all()
    
    image_paths = [glyph.foreignGlyph.glyphFile.path for glyph in selected_images]

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for image_path in image_paths:
            zip_file.write(image_path, os.path.basename(image_path))

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename=selected_images.zip'

    return response
    # return HttpResponse("Hello, World!")

def download_all_images(request):
    
    all_glyphs = Glyph.objects.all()
    
    image_paths = [glyph.glyphFile.path for glyph in all_glyphs]

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for image_path in image_paths:
            zip_file.write(image_path, os.path.basename(image_path))

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename=all_glyphs.zip'

    return response
