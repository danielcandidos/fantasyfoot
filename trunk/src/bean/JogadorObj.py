'''
Created on 12/05/2014

@author: Daniel Candido
'''

class Jogador(object):
    '''
    classdocs
    '''
    ##Strings##
    nomeJogador = ""
    ##Numeros##
    forcaJogador = 0

    def __init__(self, nome, forca):
        '''
        Constructor
        '''
        self.nomeJogador = nome
        self.forcaJogador = forca
        pass
    
    def getNome(self):
        return self.nomeJogador

    def getForca(self):
        return self.forcaJogador

    def setNome(self, value):
        self.nomeJogador = value

    def setForca(self, value):
        self.forcaJogador = value