from django.db import models

# Create your models here.

class Glyph(models.Model):
    #id
    id = models.IntegerField(primary_key=True)
    
    # date/time creation
    pub_date = models.DateTimeField()

    #parola
    parola = models.CharField(max_length=200)

    #categoria semantica
    categoria_semantica = models.CharField(max_length=200)

    #funzione grammaticale
    funzione_grammaticale = models.CharField(max_length=200)

    #figura retorica
    figura_retorica = models.CharField(max_length=200)

    # file .svg
    # glyphFile = models.FileField(upload_to="glyphs/")

    def __str__(self):
        return f"{self.id : 04d} – {self.parola}"


