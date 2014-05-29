'''
Created on 12/05/2014

@author: Daniel Candido
'''
from bean.EquipeObj import Equipe

class Partida(object):
    '''
    classdocs
    '''
    ##Equipes##
    eqp1 = Equipe(None)
    eqp2 = Equipe(None)
    ##Strings##
    nomeDoJog, arbitro = "", ""
    ##Numeros##
    grauApoio = 0

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def getArbitro(self):
        return self.arbitro    
        
    def getEqp1(self):
        return self.eqp1

    def getEqp2(self):
        return self.eqp2
    
    def getTitulo(self):
        return self.nomeDoJog
    
    def getApoio(self):
        return self.grauApoio
    
    def setEqp1(self, value):
        self.eqp1 = value

    def setEqp2(self, value):
        self.eqp2 = value
    
    def setArbitro(self, value):
        self.arbitro = value
    
    def setApoio(self, value):
        self.grauApoio = value

    def gerarTitulo(self):
        self.nomeDoJog = str(self.eqp1.getNome())+" x "+str(self.eqp2.getNome())
