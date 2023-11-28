from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from coreApp.models import Glyph, SelectedImage
from coreApp.form import GlyphFilterForm
import io
import zipfile
import os

from django.utils.translation import get_language, activate

from django.shortcuts import redirect

def index(request):
    if not request.session.session_key:
        request.session.create()
        print('!!! NEW SESSION !!!')

    print(request.session.session_key)

    return render(request, 'index.html')

def glifi(request):
    # Get the current session key
    session_key = request.session.session_key
    session_instance = Session.objects.get(session_key=session_key)

    GLYPHS = Glyph.objects.all().order_by('parola')
    SELECTED_IMAGES_FOR_SESSION = SelectedImage.objects.filter(session=session_instance)
    
    form = GlyphFilterForm(request.GET)
    
    
    if request.method == "GET":
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

        selected_image_ids = request.POST.getlist("selected_images")
        # for image_id in selected_image_ids:
        #     selected_image = SelectedImage(foreignGlyph_id=image_id,
        #                                            session=session_instance)
        #     selected_image.save()

        for image_id in selected_image_ids:
            try:
                SelectedImage.objects.get(foreignGlyph_id=image_id,
                                          session=session_instance)
            # Handle the existing entry (e.g., update or skip)
            except:
                # Create a new SelectedImage instance
                selected_image = SelectedImage(foreignGlyph_id=image_id,
                                               session=session_instance)
                selected_image.save()

    context = {
        'GLYPHS': GLYPHS,
        'FORM': form,
        "SELECTED_GLYPHS": SELECTED_IMAGES_FOR_SESSION,
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

    # Get the current session key
    session_key = request.session.session_key

    # Retrieve the corresponding Session instance
    session_instance = Session.objects.get(session_key=session_key)

    # Filter SelectedImage instances based on the session
    selected_images_for_session = SelectedImage.objects.filter(session=session_instance)

    
    image_paths = [glyph.foreignGlyph.glyphFile.path for glyph in selected_images_for_session]

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for image_path in image_paths:
            zip_file.write(image_path, os.path.basename(image_path))

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename=selected_images.zip'
    
    # Clear previously selected images for the current session
    SelectedImage.objects.filter(session=session_instance).delete()

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
