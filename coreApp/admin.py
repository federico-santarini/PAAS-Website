from django.contrib import admin
from .models import Glyph, SelectedImage
from django.contrib.sessions.models import Session

class GlyphAdmin(admin.ModelAdmin):
    list_filter = (
        'approvato',
        'variante',
        'categoria_semantica',
        'funzione_grammaticale',
        'figura_retorica',
        'presenza_umana'



    )
    list_display = (
                    'approvato',
                    'id',
                    'parola',
                    'variante',
                    'id_variante',                    
                    'parola_ENG',
                    'categoria_semantica',
                    'funzione_grammaticale',
                    'figura_retorica',
                    'presenza_umana'
                    )
    
    list_editable = (
                    'categoria_semantica',
                    'funzione_grammaticale',
                    'figura_retorica',
                    'presenza_umana',
                    'parola_ENG',


                    )
    list_display_links = (
                    'id', 
                    )
    
    readonly_fields = ('created_at','modified_at')
    
    fieldsets = [
        ("Status",{
            'fields':('approvato','created_at','modified_at'),
        }),

        ('Basic Informations', {
            'fields': (('id','id_variante','variante'),
                       ('parola', 'parola_ENG')
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
