from django import forms
from coreApp.models import Glyph
from django.utils.translation import gettext_lazy as _
    
class GlyphFilterForm(forms.Form):
    
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),)

    categorieSemantiche = forms.MultipleChoiceField(
        choices=Glyph.CATEGORIE_SEMANTICHE,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-to-hide checkbox-save-state'}),
        required=False,
        label=_("Categoria semantica"),
    )

    funzioniGrammaticali = forms.MultipleChoiceField(
        choices=Glyph.FUNZIONI_GRAMMATICALI,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-to-hide checkbox-save-state'}),
        required=False,
        label=_("Funzione grammaticale"),
    )