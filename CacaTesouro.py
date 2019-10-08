import random
import time

def cabecalho():

   print("|==================================================|")
   print("|                  CAÇA AO TESOURO                 |")
   print("|               (por Gabriel e Thomas)             |")
   print("|==================================================|")
cabecalho()
time.sleep(0.8)
print ('\nBem vindo,Pirata \nVamos iniciar nossa aventeura!!!\n')

#CRIANDO A MATRIZ PARA O JOGADOR
matrizinv = [[ '' , '' , '' , '' ],
             [ '' , '' , '' , '' ],
             [ '' , '' , '' , '' ],
             [ '' , '' , '' , '' ]]
#CRIANDO A MATRIZ PARA SELECIONAR OS BURACOS,TESOUROS E NUMEROS INTEIROS
matriz = [[ '' , '' , '' , '' ],
          [ '' , '' , '' , '' ],
          [ '' , '' , '' , '' ],
          [ '' , '' , '' , '' ]]
#CRIANDO MATRIZ PARA O JOGADOR SE SITUAR ONDE VAI JOGAR
def Imprimir_exemplo(matriz):
   matrizexemplo = [[ ' ' , ' A ' , ' B ' , ' C ' , ' D ' ],
                    [ '1' , '[ ]' , '[ ]' , '[ ]' , '[ ]' ],
                    [ '2' , '[ ]' , '[ ]' , '[ ]' , '[ ]' ],
                    [ '3' , '[ ]' , '[ ]' , '[ ]' , '[ ]' ],
                    [ '4' , '[ ]' , '[ ]' , '[ ]' , '[ ]' ]]
   for i in range(5):
      for j in range(5):
         print(matrizexemplo[i][j], end = '')
      print()
   return matrizexemplo
#CRIANDO PLACAR DE PONTUAÇÃO
def placar():
   print("")
   print("|==================================================|") 
   print("|* ~~   *   ~~  *  --> PLACAR <--  *  ~~   *   ~~ *|")
   print("|                                                  |")
   print("|  PIRATA 1:["+str(jogador1)+"]                     ")
   print("|  PONTUAÇÃO[{}]                    ".format (pontj1))
   print("|                                                  |")
   print("|  PIRATA 2:["+str(jogador2)+"]                     ")
   print("|  PONTUAÇÃO[{}]                    ".format (pontj2))
   print("|                                                  |")
   print("|==================================================|")
   print("")
 
pos_letras = ['A','B','C','D','a','b','c','d']
#CRIANDO FUNÇÕES PARA TRATAMENTO DE ERROS
def find (pos_i):
   listanum= [1,2,3,4]
   for i in range (len(listanum)):
      if listanum [i]== pos_i:
         return True
   return False
def find2 (pos_str_j):
   listaletra= ['A','B','C','D','a','b','c','d']
   for i in range (len(listaletra)):
      if listaletra[i]==pos_str_j:
         return True
   return False

#criando váriaveis
pontj1=0
pontj2=0
t=0
b=0
linha=0
coluna=0
x=True
menu = 1
contjogadas=0

while (t<6):        #colocando tesouros na matriz
   aux1=random.randint (0,3)
   aux2=random.randint (0,3)
   if (matriz[aux1][aux2] == ''):
       matriz [aux1][aux2]= 't'
       t +=1
while (b<3):       #colocando buracos na matriz
   aux1=random.randint (0,3)
   aux2=random.randint (0,3)
   if (matriz[aux1][aux2] == ''):
       matriz [aux1][aux2]= 'b'
       b +=1
while (coluna<=3):#colocando numeros inteiros na matriz
   linha = 0
   while(linha<=3):
      cont = 0
      if(matriz[linha][coluna] != 't' and matriz[linha][coluna] != 'b'):
         if(coluna-1>=0 and matriz[linha][coluna-1] == 't'):
            cont = cont+1
         if(coluna+1<=3 and matriz[linha][coluna+1] == 't'):
            cont = cont+1
         if(linha-1>=0 and matriz[linha-1][coluna] == 't'):
            cont = cont+1
         if(linha+1<=3 and matriz[linha+1][coluna] == 't'):
            cont = cont+1
         matriz[linha][coluna] = cont
      linha = linha+1
   coluna = coluna+1
while (x==True): #CRIANDO MENU E RECEBENDO INFORMAÇÕES DO JOGADOR
   time.sleep(1.2)
   print("Carregando...")
   time.sleep(1.5)
   print("\n*~~~~~~~ MENU ~~~~~~~* \n <[1]> = JOGAR \n <[2]> = DICAS \n <[3]> = SAIR\n")
   menu = input("[MENU] O que vamos fazer? ")
   if menu == '1':
      print("Aguarde...")
      time.sleep(0.8)
      print("\nEntão vamos lá! ...\nDesafie alguém e vamos a caçada!\n")
      time.sleep(0.8)
      jogador1 = input('[Jogador 1] --> Digite seu nome: ')
      time.sleep(0.3)
      jogador2 = input('[Jogador 2] --> Digite seu nome: ')
      time.sleep(0.3)
      print("\nCarregando..")
      time.sleep(2)
      print("Preparando tabuleiro..")
      time.sleep(2)
      print("Embaralhando cartas...")
      time.sleep(2)
      print('\nAtenção piratas, observem o tabuleiro abaixo antes de escolher uma carta:\n')
      time.sleep(0.3)
      Imprimir_exemplo(matriz)
   if menu == '2':
      print("Carregando dicas...")
      time.sleep(1.2)
      print("\n~O jogo é multiplayer; \n~Tesouro encontrado:+100 pontos;\n~Buraco encontrado:-50 pontos;\n~Números inteiros mostra a quantidade de tesouro que tem nas posições horizontais e verticais próximas a ele;\n~O jogo termina quando todas as cartas forem viradas;\n~Vence o jogador com maior pontuação.")
      time.sleep(1)
      voltarmenu = input('\nDeseja voltar o MENU? \n <[1]> = SIM \n <[2]> = NÃO: ')
      if (voltarmenu == '2'):
         x = False
         time.sleep(1)
         print("\nFechando o programa...até a próxima pirata! \n Finalizando...")
         time.sleep(2)
      else:
         continue
   if menu == '3':
      time.sleep(0.4)
      sair = input('\nTem certeza que deseja sair ? \n[SIM] - 1 \n[NÃO] - 2: ')
      if (sair == '1'):
         x = False
         time.sleep(1.2)
         print("\nFechando o programa...até a próxima pirata!")
         time.sleep(1.3)
         print("Finalizando...")
         time.sleep(1.5)
      else:
         continue

   while menu == '1': #INICIANDO O JOGO
      print("")
      while(contjogadas == 0):
         contjogadasj1 = 1
         contjogadasj2 = 1
         while (contjogadasj1 != 0):#VEZ DO JOGADOR1
            time.sleep(3)
            print("Pirata {}, aguarde a sua vez...".format(jogador1))
            time.sleep(2)
            print('\n*>>> Sua vez pirata {}! <<<*'.format(jogador1))
            print ('Vamos caçar os tesouros!!!')
            time.sleep(0.2)
            pos_i = int(input("\nDigite a posição da linha da carta de 1 a 4: "))
            if (find(pos_i)==False):#TRATAMENTO DE ERRO DOS NUMEROS
               time.sleep(0.2)
               print ('\nEsta posição não existe.\nPreste mais atenção pirata, digite corretamente a linha e a coluna desejada!')
               continue
            pos_j = 0
            time.sleep(0.2)
            pos_str_j = str(input("Digite a posição da coluna da carta de A a D: "))
            if (find2(pos_str_j) ==False):#TRATAMENTO DE ERRO DAS LETRAS
               time.sleep(0.2)
               print('\nEsta posição não existe.\nPreste mais atenção pirata, digite corretamente a linha e a coluna desejada!')
               continue
            
            if pos_i > 0:#COVERTENDO NUMEROS PARA LETRA
               pos_i = pos_i - 1
            if pos_str_j in pos_letras:
               if pos_str_j == pos_letras[0] or pos_str_j == pos_letras[4]:
                  pos_j = 0
               if pos_str_j == pos_letras[1] or pos_str_j == pos_letras[5]:
                  pos_j = 1
               if pos_str_j == pos_letras[2] or pos_str_j == pos_letras[6]:
                  pos_j = 2
               if pos_str_j == pos_letras[3] or pos_str_j == pos_letras[7]:
                  pos_j = 3
                  
            if matrizinv[pos_i][pos_j] == 't':#AVALIAÇÃO DA CARTA SOLICITADA DO JOGADOR 
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue
            if matrizinv[pos_i][pos_j] == 'b':
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue
            if matrizinv[pos_i][pos_j] == 0 or matrizinv[pos_i][pos_j] == 1 or matrizinv[pos_i][pos_j] == 2 or matrizinv[pos_i][pos_j] == 3:
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue
            
            time.sleep(1)
            print("\n{} está cavando...".format(jogador1))
            time.sleep(1)
            print("e... BUUFFF")
            time.sleep(0.6)
            print("O que será que você encontrou {}?\n".format(jogador1))
            matrizinv[pos_i][pos_j] = matriz[pos_i][pos_j]
            time.sleep(0.6)
            for i in range(4):
               for j in range(4):
                  print('[{}]'.format(matrizinv[i][j]), end = '')
               print ()
            #CONTANDO PONTUAÇÃO DO JOGADOR1
            if (matrizinv[pos_i][pos_j]== 't'):
               pontj1=pontj1+100
            if (matrizinv[pos_i][pos_j]== 'b'):
               if (pontj1==0):
                  pontj1=0
               else:
                  pontj1=pontj1-50
                  
            if (matrizinv[i][j] != ''):#AVALIANDO CARTA SOLICITADA PELO JOGADOR E AVALIANDO O JOGADOR
               if pontj1 > pontj2:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {} e venceu o jogo com {} pontos, parabéns!!!".format(jogador1,pontj1))
                  time.sleep(0.6)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e venceu o jogo!".format(jogador1,pontj1))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
               elif pontj1 < pontj2:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {}, mas não venceu, parabéns mesmo assim! Volte novamente outra vez para jogar!!!".format(jogador1))
                  time.sleep(0.3)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e venceu o jogo!".format(jogador2,pontj2))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
               elif pontj1 == pontj2:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {} e o jogo terminou empate,mesmo assim parabéns piratas! Voltem novamente outra vez para jogar!!!".format(jogador2))
                  time.sleep(0.3)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e {} fez {} pontos e o jogo terminou empate!".format(jogador1,pontj1,jogador2,pontj2))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
               x = False
               menu = 4
               contjogadas = 1
               contjogadasj1 = 0
               
            if contjogadasj1 != 0:
               time.sleep(3)
               placar()
            contjogadasj1=0
            
         while (contjogadasj2 != 0):#VEZ DO JOGADOR2
            time.sleep(3)
            print("Pirata {}, aguarde a sua vez...".format(jogador2))
            time.sleep(2)
            print('\n*>>> Sua vez pirata {}! <<<*'.format(jogador2))
            print ('Vamos caçar os tesouros!!!')
            time.sleep(0.3)
            pos_i = int(input("\nDigite a posição da linha da carta de 1 a 4: "))
            if (find(pos_i)==False):#TRATAMENTO DE ERRO DOS NUMEROS
               time.sleep(0.3)
               print ('\nEsta posição não existe.\nPreste mais atenção pirata, digite corretamente a linha e a coluna desejada!')
               continue
            pos_j = 0
            time.sleep(0.3)
            pos_str_j = str(input("Digite a posição da coluna da carta de A a D: "))
            if (find2(pos_str_j) ==False):#TRATAMENTO DE ERRO DAS LETRAS
               time.sleep(0.3)
               print('\nEsta posição não existe.\nPreste mais atenção pirata, digite corretamente a linha e a coluna desejada!')
               continue
            #CONVERTENDO NUMEROS PARA LETRA
            if pos_i > 0:
               pos_i = pos_i - 1
            if pos_str_j in pos_letras:
               if pos_str_j == pos_letras[0] or pos_str_j == pos_letras[4]:
                  pos_j = 0
               if pos_str_j == pos_letras[1] or pos_str_j == pos_letras[5]:
                  pos_j = 1
               if pos_str_j == pos_letras[2] or pos_str_j == pos_letras[6]:
                  pos_j = 2
               if pos_str_j == pos_letras[3] or pos_str_j == pos_letras[7]:
                  pos_j = 3
            #AVALIAÇÃO DA CARTA SOLICITADA DO JOGADOR
            if matrizinv[pos_i][pos_j] == 't':
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue
            if matrizinv[pos_i][pos_j] == 'b':
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue
            if matrizinv[pos_i][pos_j] == 0 or matrizinv[pos_i][pos_j] == 1 or matrizinv[pos_i][pos_j] == 2 or matrizinv[pos_i][pos_j] == 3:
               time.sleep(0.3)
               print('\nEsta carta ja foi virada pirata :(')
               print('Preste mais atenção, digite corretamente a linha e a coluna desejada!')
               continue

            time.sleep(1)
            print("\n{} está cavando...".format(jogador2))
            time.sleep(1)
            print("e... BUUFFF")
            time.sleep(0.3)
            print("O que será que você encontrou {}?\n".format(jogador2))
            matrizinv[pos_i][pos_j] = matriz[pos_i][pos_j]
            time.sleep(0.3)
            for i in range(4):
               for j in range(4):
                  print('[{}]'.format(matrizinv[i][j]), end = '')
               print ()
            #CONTANDO PONTUAÇÃO DO JOGADOR2
            if (matrizinv[pos_i][pos_j]== 't'):
               pontj2=pontj2+100
            if (matrizinv[pos_i][pos_j]== 'b'):
               if (pontj2==0):
                  pontj2=0
               else:
                  pontj2=pontj2-50
             #AVALIANDO CARTA SOLICITADA PELO JOGADOR E AVALIANDO O VENCEDOR     
            if (matrizinv[i][j] != ''):
               if pontj2 > pontj1:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {} e venceu o jogo com {} pontos, parabéns!!!".format(jogador2,pontj2))
                  time.sleep(0.3)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e venceu o jogo!".format(jogador2,pontj2))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
               elif pontj2 < pontj1:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {}, mas não venceu, parabéns mesmo assim! Volte novamente outra vez para jogar!!!".format(jogador2))
                  time.sleep(0.3)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e venceu o jogo!".format(jogador1,pontj1))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
               elif pontj1 == pontj2:
                  time.sleep(1)
                  print("\nVocê virou a última carta pirata {} e o jogo terminou empate,mesmo assim parabéns piratas! Voltem novamente outra vez para jogar!!!".format(jogador2))
                  time.sleep(0.3)
                  print("\nParabéns pela aventura piratas, confiram abaixo como ficou o placar do jogo:")
                  time.sleep(1)
                  print("\n*>>> {} fez {} pontos e {} fez {} pontos e o jogo terminou empate!".format(jogador1,pontj1,jogador2,pontj2))
                  placar()
                  print("\nFechando o programa...até a próxima piratas! \n Finalizando...")
                  
               x = False
               menu = 4
               contjogadas = 1
               contjogadasj2 = 0
               
            if contjogadasj2 != 0:
               time.sleep(3)
               placar()
            contjogadasj2=0

##       break