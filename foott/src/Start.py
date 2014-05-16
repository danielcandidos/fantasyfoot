'''
Created on 12/05/2014

@author: Daniel Candido
'''

from bean.JogadorObj import Jogador
from bean.EquipeObj import Equipe
from bean.PartidaObj import Partida
from util.RidAlg import RidAlg


if __name__ == '__main__':    
    """
    clube1 = [("Brasil A",None),("Julio",87),("Daniel",87),("Thiago",92),("David",86),("Marcelo",86),("Luis",83),\
                 ("Paulinho",84),("Oscar",85),("Neymar",89),("Fred",85),("Hulk",84)]
    clube2 = [("Brasil B",None),("Victor",86),("Maicon",85),("Henrique",85),("Dante",84),("Maxwell",84),("Ramires",84),\
                 ("Hernanes",85),("Willian",83),("Bernard",85),("Jo",79),("Fernandinho",81)]    
            
    print clube1[0][0] +"\tx \t"+ clube2[0][0] +"\n"
    
    for a in range(1,12):          
        print str(clube1[a])+"\t \t"+str(clube2[a])
        
    print ""
    
    contA=0
    contB=0
    
    for a in range(1,12):          
        contA+=clube1[a][1]
        contB+=clube2[a][1]
        #print clube1[a][1],clube2[a][1]
        
    #print contA, contB
    
    if contA>contB:
        print clube1[0][0] + " GANHOU PORRA! \O/"
    elif contB>contA:
        print clube2[0][0] + " GANHOU PORRA! \O/"
    else:
        print "EMPATE NESSE CARAI! --'"
    """
    
    print "----------------- FantasyFoot -----------------"
    print"- Insira as equipes participantes da partida! -"
    print"---- obs: a primeira equipe informada sera ----\n-- considerada a anfitria (que joga em casa) --"
    print "-----------------------------------------------\n"
    
    comando = "vai"
    
    ##loop para inicio/reinicio do jogo##
    while comando == "vai":    
        ##objeto Partida instanciado##
        partida = Partida()
        
        ##loop para insercao da equipe (nome+pesoCamisa+fase+jogadores(nome+forca))##
        for a in range(1,3):
            tempEqp = raw_input("Nome da Equipe "+str(a)+": ")
            eqp = Equipe(tempEqp)
            print ("Qual o peso da sua camisa? (0~10)")
            tempPeso = input("-> ")
            eqp.setPesoCamisa(tempPeso)
            print "Qual fase se encontra o/a "+tempEqp+" (-2/-1/0/1/2/3)"
            tempFase = input("-> ")
            eqp.setFase(tempFase)
            for b in range(1,4):
                nome = raw_input("Jogador "+str(b)+": ")
                forca = input("Forca de "+nome+": ")
                jogador = Jogador(nome,forca)
                eqp.addJogador(jogador)
            ##entrada da forca do apoio da torcida##                       
            if (a==1):
                partida.setEqp1(eqp)
                print ("Qual o grau de apoio da torcida local? (-2/-1/0/1/2/3/4)")
                apoio = input("-> ")
                partida.setApoio(apoio)
            elif (a==2):
                partida.setEqp2(eqp)
            print "" 
        
        partida.gerarTitulo()
        print partida.getTitulo()
        
        ##espera de evento para simular a partida usando algoritmo##
        t = raw_input("- Pressione ENTER para simular a partida -")
        algoritmo = RidAlg(partida)
        resultado = algoritmo.calculo()
        if resultado != None:
            print resultado.upper()+" VENCEU! \O/"
        else:
            print "DEU EMPATE!"
        
        ##loop para continuacao do jogo##    
        resp = ""
        while True:
            resp = raw_input("\nDeseja jogar novamente? (S/N) ")
            if resp == "S" or resp == "s":
                comando="vai"
                print ""
                break
            elif resp == "N" or resp == "n":
                comando="pare"
                print "- / -"
                break
    