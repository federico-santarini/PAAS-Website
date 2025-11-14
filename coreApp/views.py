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
    glyphs = Glyph.objects.all().order_by('parola')
    form = GlyphFilterForm(request.GET or None)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        categories = form.cleaned_data.get('categorieSemantiche')
        functions = form.cleaned_data.get('funzioniGrammaticali')

        # --- Filtraggio testuale dipendente dalla lingua ---
        if search:
            lang = get_language() or request.LANGUAGE_CODE or 'it'   # fallback 'it'
            if lang.startswith('en'):
                glyphs = glyphs.filter(parola_ENG__icontains=search)
            else:
                # considera qualunque lingua non-inglese come italiana
                glyphs = glyphs.filter(parola__icontains=search)
        if categories:
            glyphs = glyphs.filter(categoria_semantica__in=categories)
        if functions:
            glyphs = glyphs.filter(funzione_grammaticale__in=functions)

    context = {
        'GLYPHS': glyphs,
        'FORM': form,
    }

    # Check if this is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'glyphs_list.html', context)
    else:
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

from django.http import JsonResponse

def ajax_glyphs_view(request):
    # Your existing logic to retrieve selected glyphs
    session_key = request.session.session_key
    session_instance = Session.objects.get(session_key=session_key)
    SELECTED_IMAGES_FOR_SESSION = SelectedImage.objects.filter(session=session_instance)

    # Assuming SELECTED_IMAGES_FOR_SESSION is a list of SelectedImage instances
    data = [{'foreignGlyph': {'parola': selected_image.foreignGlyph.parola}} for selected_image in SELECTED_IMAGES_FOR_SESSION]

    return JsonResponse(data, safe=False)
