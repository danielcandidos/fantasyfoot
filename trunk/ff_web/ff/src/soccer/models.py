# -*- coding: utf-8 -*-
'''
Created on 25/05/2014
@author: Daniel
'''
from django.db import models

class Clube (models.Model):
    nome = models.CharField(max_length=30)
    
    FASE = (        ('-2','-2'),        ('-1','-1'),        ('0','0'),        ('1','1'),
        ('2','2'),        ('3','3'),        ('4','4')
    )
    fase = models.IntegerField(max_length=1, choices=FASE)
    
    PESO = (        ('0','0'),        ('1','1'),        ('2','2'),        ('3','3'),        ('4','4'),        ('5','5'),
        ('6','6'),        ('7','7'),        ('8','8'),        ('9','9'),        ('10','10')
    )
    peso = models.IntegerField(max_length=1, choices=PESO)
    
    def __unicode__(self): 
        return u"%s" %(self.nome) 

class Jogador (models.Model):
    nome = models.CharField(max_length=30)
    
    FORCA = (        ('10','10'),        ('20','20'),        ('25','25'),        ('35','35'),        ('40','40'),
        ('50','50'),        ('55','55'),        ('60','60'),        ('65','65'),        ('75','75'),        ('80','80'),
        ('90','90'),        ('100','100'),        ('110','110'),        ('120','120'),        ('130','130'),        ('140','140'),
    )
    forca = models.IntegerField(max_length=3, choices=FORCA)
    
    clube = models.ForeignKey(Clube)
    
    def __unicode__(self):
        return u"%s - %s" %(self.nome, self.clube.nome)