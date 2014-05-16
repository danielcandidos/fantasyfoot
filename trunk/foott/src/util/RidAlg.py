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
    ##Dicionarios##
    dicHome= {"forca":None,"torcida":None,"pesoCamisa":None,"fase":None,"clima":None,"tatica":None}
    dicAway= {"forca":None,"pesoCamisa":None,"fase":None,"clima":None,"tatica":None}
    
    def __init__(self, jogo):
        '''
        Constructor
        '''
        self.partida = jogo
        
        ##gravando as forcas dos jogadores##
        intA, intB = 0,0        
        for jog in self.partida.getEqp1().getElenco():
            intA+=jog.getForca()
        for jog in self.partida.getEqp2().getElenco():
            intB+=jog.getForca()
        self.dicHome['forca']=intA
        self.dicAway['forca']=intB
        
        ##gravando o peso das camisas##
        self.dicHome['pesoCamisa'] = self.partida.getEqp1.getPesoCamisa()
        self.dicAway['pesoCamisa'] = self.partida.getEqp2.getPesoCamisa()
        
        ##gravando a fase das equipes##
        self.dicHome['fase'] = self.partida.getEqp1.getFase()
        self.dicAway['fase'] = self.partida.getEqp2.getFase()
                
        pass
    
    ##calculo do venvedor provavel da partida##
    def calculo(self):
        forca1=self.dicHome['forca']
        forca2=self.dicAway['forca']
        
        if ((forca1 * ((self.dicHome['fase']-self.dicAway['fase'])*(0.1/5))\
            + forca1 * ((self.dicHome['pesoCamisa']-self.dicAway['pesoCamisa'])*(0.1/10))\
            + (forca1 *((self.partida.getApoio()*0.05)+1)))>forca2):
            return self.partida.getEqp1().getNome()
        elif ((forca1 * ((self.dicHome['fase']-self.dicAway['fase'])*(0.1/5))\
            + forca1 * ((self.dicHome['pesoCamisa']-self.dicAway['pesoCamisa'])*(0.1/10))\
            + (forca1 *((self.partida.getApoio()*0.05)+1)))<forca2):
            return self.partida.getEqp2().getNome()
        else:
            return None
        
    