from django import forms
from coreApp.models import Glyph

class GlyphFilterForm(forms.Form):
    
    search = forms.CharField(max_length=100, required=False)

    categorieSemantiche = forms.MultipleChoiceField(
        choices=Glyph.CATEGORIE_SEMANTICHE,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-save-state'}),
        required=False,
        label="Categoria semantica",
    )

    funzioniGrammaticali = forms.MultipleChoiceField(
        choices=Glyph.FUNZIONI_GRAMMATICALI,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-save-state'}),
        required=False,
        label="Funzione grammaticale",
    )