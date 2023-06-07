titulo = 'Adivinhe um número'
'''
Data: 25/03/2023
Autor: Daniel
Descrição: Jogo para advinhar um número informado
pelo usuário (10 tentativas)
'''
print('Seja bem vindo ao programa ' + titulo)

import random
import time

numero_pc = random.randint(0,10000)

vitoria = False

for tentativa in range(1,11):
      print('Tentativa número ' + str(tentativa))
      numero_usuario = int(input('Digite um número: '))
      
      time.sleep(0.3)
      print('Analisando o número',end='')
      time.sleep(0.5)
      print('.',end='')
      time.sleep(0.5)
      print('.',end='')
      time.sleep(0.5)
      print('.',end='')
      time.sleep(1)
      print()


      if numero_pc > numero_usuario:
            print('O número é maior')
      elif numero_pc < numero_usuario:
            print('O número é menor')
      else:
            print('Parabéns!!! Você acertou!!!')
            vitoria = True
            break
      print('\n#################################\n')

if vitoria == False:
      print('Você perdeu, o número era ' + str(numero_pc))