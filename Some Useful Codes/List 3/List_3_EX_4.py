titulo = 'Jogo de luta'
'''
Data: 25/03/2023
Autor: Cleber
Descrição: Jogo de Luta entre usuario e PC
Faça um jogo de batalha entre você e o computador:
Cada um dos jogadores inicia com 10 pontos de vida.

Neste jogo você deverá comparar o poder de combate em cada turno, quem ganhar desfere o ataque no oponente causando o dano respectivo.

Você tem dois ataques, que poderá selecionar no início de cada rodada:
1.	Cabeçada: Tem poder de combate 3, se ganhar tira 3 de vida do oponente e toma 1 de dano.
2.	Soco: Tem poder de combate aleatório (jogar no dado D6) e caso ganhe causa dano aleatório (jogar no dado D6).

O computador tem apenas o ataque Soco.

Quem chegar a 0 pontos de vida perde o jogo.

'''
print('Seja bem vindo ao programa ' + titulo)

import random
import time

vida_usuario = 10
vida_pc = 10

while True:
      escolha = input('Escolha (S) para Soco, (C) para cabeçada\
,\n(I) para Informações e (X) para sair\n')

      if escolha == 'X':
            print('Finalizando o Jogo')
            time.sleep(1)
            break
      elif escolha == 'I':
            time.sleep(0.1)
            print('\n##################################')
            print('(S) --> Soco')
            time.sleep(0.2)
            print('Poder de Combate (aleatório): 1 a 6')
            time.sleep(0.2)
            print('Dano (aleatório) : 1 a 6')
            time.sleep(0.5)
            print('\n(C) --> Cabeçada')
            time.sleep(0.2)
            print('Poder de Combate: 3')
            time.sleep(0.2)
            print('Dano: 3')
            time.sleep(0.2)
            print('Se ganhar o combate, recebe 1 de dano e causa 3 de dano no oponente')
            time.sleep(0.2)
            print('##################################\n')
            time.sleep(0.5)
            continue
      elif escolha != 'S' and escolha != 'C':
            print('Opção inválida\n')
            time.sleep(0.5)
            continue

      if escolha == 'S':
            poder_usuario = random.randint(1,6)
            dano_usuario = random.randint(1,6)
      elif escolha == 'C':
            poder_usuario = 3
            dano_usuario = 3
      
      print('Poder Usuário',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(0.5)
      print(' ' + str(poder_usuario))
      poder_pc = random.randint(1,6)
      dano_pc = random.randint(1,6)
      time.sleep(0.5)
      print('Poder PC',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(0.5)
      print(' ' + str(poder_pc)+ '\n')

      print('Analisando',end='')
      for i in range(3):
            time.sleep(0.3)
            print('.',end='')
      time.sleep(0.5)
      if poder_usuario > poder_pc:
            print('Você ganhou o turno')
            time.sleep(0.5)
            print('Você desferiu ' + str(dano_usuario) + ' de dano')
            vida_pc -= dano_usuario
            if escolha == 'C':
                  print('Você recebeu 1 de dano por usar Cabeçada')
                  vida_usuario -= 1
      elif poder_usuario < poder_pc:
            print('Você perdeu o turno')
            time.sleep(0.5)
            print('Você recebeu ' + str(dano_pc) + ' de dano')
            vida_usuario -= dano_pc
      else:
            print('Combate empatou')
      
      time.sleep(0.5)
      print('\n##################################')
      print('Vida Usuário: ' + str(vida_usuario))
      print('Vida PC: ' + str(vida_pc))
      print('##################################\n')
      time.sleep(0.5)

      if vida_usuario <= 0:
            print('Você perdeu o jogo')
            time.sleep(1)
            break
      elif vida_pc <= 0:
            print('Você ganhou o jogo')
            time.sleep(1)
            break

      