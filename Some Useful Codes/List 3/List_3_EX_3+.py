titulo = 'Pedra, Papel e Tesoura'
'''
Data: 25/03/2023
Autor: CLEBER
Descrição: Jogo de Pedra, Papel e Tesoura com outra lógica.
No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas.
'''
print('Seja bem vindo ao programa ' + titulo)

import random
import time

num_vit = 0
num_emp = 0
num_der = 0

while True:
      escolha_usuario = input('Escolha (P) para Papel, (R) para Pedra, (T) para Tesoura ou (X) para sair\n').upper()
      
      if escolha_usuario == 'X':
            print('Finalizando jogo...')
            time.sleep(1)
            break
      if escolha_usuario != 'P' and\
            escolha_usuario != 'R' and\
            escolha_usuario != 'T':
            print('Opção incorreta')
            time.sleep(1)
            continue
      time.sleep(0.5)
      print('Você escolheu',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(1)
      if escolha_usuario == 'P':
            print('\n Papel')
      elif escolha_usuario == 'R':
            print('\n Pedra')
      else:
            print('\n Tesoura')

      numero_pc = random.randint(1,3)
      if numero_pc == 1:
            escolha_pc = 'P'
      elif numero_pc == 2:
            escolha_pc = 'R'
      elif numero_pc == 3:
            escolha_pc = 'T'

      time.sleep(0.5)
      print('O PC escolheu',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(1)

      if escolha_pc == 'P':
            print('\n Papel')
      elif escolha_pc == 'R':
            print('\n Pedra')
      else:
            print('\n Tesoura')
      
      print('Analisando',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(1)
      if escolha_usuario == 'P':
            if escolha_pc == 'P':
                  num_emp += 1
                  print('Empate')
            elif escolha_pc == 'R':
                  num_vit += 1
                  print('Você venceu!')
            else:
                  num_der += 1
                  print('Você perdeu!')
      elif escolha_usuario == 'R':
            if escolha_pc == 'P':
                  num_der += 1
                  print('Você perdeu!')
            elif escolha_pc == 'R':
                  num_emp += 1
                  print('Empate')
            else:
                  num_vit += 1
                  print('Você venceu!')
      elif escolha_usuario == 'T':
            if escolha_pc == 'P':
                  num_vit += 1
                  print('Você venceu!')
            elif escolha_pc == 'R':
                  num_der += 1
                  print('Você perdeu!')
            else:
                  num_emp += 1
                  print('Empate')
      
      time.sleep(1)
      print('\n##########################')
      print('Vitórias: ' + str(num_vit))
      time.sleep(0.3)
      print('Empates: ' + str(num_emp))
      time.sleep(0.3)
      print('Derrotas: ' + str(num_der))
      time.sleep(0.3)
      print('##########################\n')
      time.sleep(2)