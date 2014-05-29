'''
Created on 25/05/2014

@author: Daniel
'''
from django import forms

from soccer.models import Clube, Jogador

class FormClube(forms.ModelForm):
    class Meta:
        model = Clube

class FormJogador(forms.ModelForm):
    class Meta:
        model = Jogador
        