'''
Data: 25/03/2023
Autor: Cleber Belisse
Descrição:
Faça um programa para adivinhar um número de 0 a 10000.
Se você errar o computador deverá responder se é mais ou menos.
Se você errar 10 vezes você perde o jogo.
#OBS: Podemos acertar qualquer numero escolhido de 1 a 100000 com 14 tentativas, divida e veja se
é menor ou maior ai faça isso sucessivamente.
'''
import random as rd
import time
titulo = '"Adivinhando um número de 1 a 10000"'
print('Bem vindo ao programa ' + titulo)

numero_escolhido = rd.randint(1,10000)
print(numero_escolhido)
vitoria = False

'''
Note que no range abaixo colocamos de 1 a 11 pra poder informar o usuário em qual tentativa ele está
pois se usar somente o 10 a contagem começa do 0 e nao existe tentativa 0.
'''
for tentativa in range(1,11): 
    print('Tentativa '+ str(tentativa))
    chute = int(input('Escolha um número:'))
    time.sleep(0.3) #0.3 segundo de tempo
    '''
    print('Analisando o número ', end='')
    time.sleep(0.3)
    print('.',end='')
    time.sleep(0.4)
    print('.',end='')
    time.sleep(0.4)
    print('.', end='')
    time.sleep(0.5)
    print()
    '''

    if chute < numero_escolhido:
        print('Errrrrrrroooou')
        print('Você escolheu um número menor do que o número correto! ')

    elif chute > numero_escolhido:
        print('Errrrrrrroooou')
        print('Você escolheu um número maior do que o número correto! ')
    
    else:
        vitoria = True
        print('Acertou!')
        print('\n')
        break
    print('\n###################################')
    print('\n')

if vitoria == False:
    print('Suas tentativas acabaram o número era ' + str(numero_escolhido))