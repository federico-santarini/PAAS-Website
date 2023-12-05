from django.db import models
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _




# Create your models here.

class Glyph(models.Model):
    FIGURE_RETORICHE = [
        ("Analogia", _("Analogia")),
        ("Letterale", _("Letterale")),
        ("Metonimina", _("Metonimina")),
        ("Sineddoche", _("Sineddoche")),
        ("Simbolico", _("Simbolico")),
    ]    
    FUNZIONI_GRAMMATICALI = [
        ("Sostantivo", _("Sostantivo")),
        ("Verbo", _("Verbo")),
        ("Avverbio", _("Avverbio")),
        ("Parola grammaticale", _("Parola grammaticale")),
        ("Aggettivo", _("Aggettivo")),
    ]

    CATEGORIE_SEMANTICHE = [
        ("Abbigliamento", _("Abbigliamento")),
        ("Altro", _("Altro")),
        ("Animali", _("Animali")),
        ("Azioni", _("Azioni")),
        ("Bevande", _("Bevande")),
        ("Condizioni metereologiche", _("Condizioni metereologiche")),
        ("Mestieri", "Mestieri"),
        ("Mezzi di trasporto", _("Mezzi di trasporto")),
        ("Oggetti", _("Oggetti")),
        ("Saluti", _("Saluti")),
        ("Sostanze", _("Sostanze")),
        ("Sport", _("Sport")),
        ("Tempo", _("Tempo")),
    ] 


    # date/time creation
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    #id
    id = models.IntegerField(primary_key=True, default=0)
    id_variante = models.IntegerField(default=0)
    variante = models.BooleanField(default=False,verbose_name="is alternative")

    #parola
    parola = models.CharField(max_length=200)
    parola_ENG = models.CharField(max_length=200, default="")

    #categoria semantica
    categoria_semantica = models.CharField(max_length=200,
                                           choices=CATEGORIE_SEMANTICHE,
                                           )
    #funzione grammaticale
    funzione_grammaticale = models.CharField(max_length=200,
                                             choices=FUNZIONI_GRAMMATICALI,
                                             )

    #figura retorica
    figura_retorica = models.CharField(max_length=200,
                                           choices=FIGURE_RETORICHE,
                                           )
    presenza_umana = models.BooleanField(default=False)
    approvato = models.BooleanField(default=True)

    # file .svg
    glyphFile = models.FileField(upload_to="glyphs/")

    def __str__(self):
        return f"{self.id : 04d} – {self.parola}"


class SelectedImage(models.Model):
    foreignGlyph = models.ForeignKey(Glyph, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.foreignGlyph.id : 04d} – {self.foreignGlyph.parola}"

    class Meta:
        unique_together = ('foreignGlyph', 'session')
