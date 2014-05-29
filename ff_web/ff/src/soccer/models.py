from django.db import models

# Create your models here.

class Clube (models.Model):
    nome = models.CharField(max_length=30)
    fase = models.IntegerField(max_length=1)
    peso = models.IntegerField(max_length=1)
    
    def __unicode__(self):
        return u"%s" %(self.nome)

class Jogador (models.Model):
    nome = models.CharField(max_length=30)
    forca = models.IntegerField(max_length=3)
    clube = models.ForeignKey(Clube)
    
    def __unicode__(self):
        return u"%s - %s" %(self.nome, self.clube.nome)