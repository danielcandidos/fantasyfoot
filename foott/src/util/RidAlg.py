'''
Created on 12/05/2014

@author: Daniel Candido
'''
from bean.PartidaObj import Partida
from bean.EquipeObj import Equipe
from bean.JogadorObj import Jogador

class RidAlg(object):
    '''
    classdocs
    '''
    ##Partida##
    partida = Partida()
    ##Numeros##
    victoryHope = 0
    ##Lists####
    list = []
    
    def __init__(self, jogo):
        '''
        Constructor
        '''
        self.partida = jogo
        pass
    
    ##calculo do venvedor provavel da partida##
    def calculo(self):
        ##contadores de forcas dos jogadores##
        intA, intB = 0,0
        
        for jog in self.partida.getEqp1().getElenco():
            intA+=jog.getForca()
        for jog in self.partida.getEqp2().getElenco():
            intB+=jog.getForca()
        
        ##definicao do provavel campeao com adicao do fator torcida##
        if (intA+(self.partida.getApoio()*10)>intB):
            return self.partida.getEqp1().getNome()
        elif (intB>intA+(self.partida.getApoio()*10)):
            return self.partida.getEqp2().getNome()
        else:
            return None
        
    