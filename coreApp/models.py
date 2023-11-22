from django.db import models
from django.contrib.sessions.models import Session


# Create your models here.

class Glyph(models.Model):
    FUNZIONI_GRAMMATICALI = [
        ("Sostantivo", "Sostantivo"),
        ("Verbo", "Verbo"),
        ("Avverbio", "Avverbio"),
        ("Parola grammaticale", "Parola grammaticale"),
        ("Aggettivo", "Aggettivo"),
    ]    
    CATEGORIE_SEMANTICHE = [
        ("Abbigliamento", "Abbigliamento"),
        ("Altro", "Altro"),
        ("Animali", "Animali"),
        ("Azioni", "Azioni"),
        ("Bevande", "Bevande"),
        ("Condizioni metereologiche", "Condizioni metereologiche"),
        ("Mestieri", "Mestieri"),
        ("Mezzi di trasporto", "Mezzi di trasporto"),
        ("Oggetti", "Oggetti"),
        ("Saluti", "Saluti"),
        ("Sostanze", "Sostanze"),
        ("Sport", "Sport"),


    ]    

    #id
    id = models.IntegerField(primary_key=True)
    # date/time creation
    pub_date = models.DateTimeField()

    #parola
    parola = models.CharField(max_length=200)

    #categoria semantica
    categoria_semantica = models.CharField(max_length=200,
                                           choices=CATEGORIE_SEMANTICHE,
                                           )
    #funzione grammaticale
    funzione_grammaticale = models.CharField(max_length=200,
                                             choices=FUNZIONI_GRAMMATICALI,
                                             )

    #figura retorica
    figura_retorica = models.CharField(max_length=200)

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
