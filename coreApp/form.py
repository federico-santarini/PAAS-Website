from django import forms
from coreApp.models import Glyph

class GlyphFilterForm(forms.Form):
    FUNZIONI_GRAMMATICALI = [
        ("Sostantivo", "Sostantivo"),
        ("Verbo", "Verbo"),
        ("Avverbio", "Avverbio"),
        ("Parola grammaticale", "Parola grammaticale"),
        ("Aggettivo", "Aggettivo"),
    ]    

    tags = forms.MultipleChoiceField(
        choices=FUNZIONI_GRAMMATICALI,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )