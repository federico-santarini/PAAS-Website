from django.contrib import admin
from .models import Glyph, SelectedImage
from django.contrib.sessions.models import Session

class GlyphAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Status",{
            'fields':('approvato',),
        }),

        ('Basic Informations', {
            'fields': (('id','id_variante','variante'),
                       ('parola',
                       'parola_ENG')
                       
                       ),
        }),

        ('Taggatura', {
            'fields': ('presenza_umana', 'figura_retorica', 'funzione_grammaticale', 'categoria_semantica'),
        }),
        ('Files', {
            'fields': ('glyphFile',),

        }),
    ]


# Register your models here.
admin.site.register(Glyph, GlyphAdmin)
admin.site.register(SelectedImage)
admin.site.register(Session)
