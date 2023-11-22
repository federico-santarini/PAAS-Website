from django.contrib import admin
from .models import Glyph, SelectedImage
from django.contrib.sessions.models import Session


# Register your models here.
admin.site.register(Glyph)
admin.site.register(SelectedImage)
admin.site.register(Session)
