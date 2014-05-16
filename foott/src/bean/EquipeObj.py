'''
Created on 12/05/2014

@author: Daniel Candido
'''
from bean.JogadorObj import Jogador

class Equipe(object):
    '''
    classdocs
    '''
    ##Strings## 
    nomeDaEquipe = ""
    ##Numeros##
    pesoCamisa,fase = 0,0
    ##Lists####
    elenco = []
    
    def __init__(self, nome):
        '''
        Constructor
        '''
        self.nomeDaEquipe = nome
        self.elenco = []
        pass

    def getPesoCamisa(self):
        return self.pesoCamisa

    def getFase(self):
        return self.fase

    def setPesoCamisa(self, value):
        self.pesoCamisa = value

    def setFase(self, value):
        self.fase = value
    
    def getNome(self):
        return self.nomeDaEquipe

    def getElenco(self):
        return self.elenco

    def setNome(self, value):
        self.nomeDaEquipe = value

    def setElenco(self, value):
        self.elenco = value
    
    def addJogador(self, jogador):
        self.elenco.append(jogador)
    
    def delJogador(self, nome):
        self.elenco
        
    def zerar(self):
        self.elenco = []
        self.nomeDaEquipe = ""
        print self.elenco
