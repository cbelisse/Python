'''
Data: 25/03/2023
Autor: Cleber Belisse
Descrição:
Data: 25/03/2023
3)	Faça um jogo de Pedra, Papel e Tesoura.
No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas.

'''
import random as rd
import time
titulo = '"Jokenpô contra a máquina"'
print('Bem vindo ao programa ' + titulo)

#print(escolha_maq)
num_empate = 0
num_vitoria = 0
num_derrota = 0

while True:
    print('Escolha as seguintes opções: \nP = Papel \nR = Pedra \nT = Tesoura \nS = Sair')
    voce = input('')

    num_maquina = rd.randint(1,3)

    if num_maquina == 1:
        escolha_maq = 'Papel'
    elif num_maquina == 2:
        escolha_maq = 'Pedra'
    elif num_maquina == 3:
        escolha_maq = 'Tesoura'

    if voce == "S":
        print('Saindo do programa')
        break
    elif voce != 'P' and\
        voce != 'T' and\
        voce != 'R':
        print('Escolha inválida. Saindo do programa.')
        break

    time.sleep(0.3)
    print('Joken',end='')
    time.sleep(0.5)
    print('nn',end='')
    time.sleep(0.5)
    print('nn',end='')
    time.sleep(0.5)
    print('pÔ',end='')
    time.sleep(1)
    print()

    
    if voce == 'P' and escolha_maq == 'Papel':
        print('Papel ' + 'x ' + escolha_maq + ' = Empate')
        num_empate += 1
    elif voce == 'R' and escolha_maq == 'Pedra':
        print('Pedra ' + 'x ' + escolha_maq + ' = Empate')
        num_empate += 1
    elif voce == 'T' and escolha_maq == 'Tesoura':
        print('Papel ' + 'x ' + escolha_maq + ' = Empate')
        num_empate += 1
    elif voce == 'P' and escolha_maq == 'Pedra':
        print('Papel ' + 'x ' + escolha_maq + ' = Papel embrulha pedra, você venceu.')
        num_vitoria += 1
    elif voce == 'R' and escolha_maq == 'Tesoura':
        print('Pedra ' + 'x ' + escolha_maq + ' = Pedra quebra tesoura, você venceu.')
        num_vitoria += 1
    elif voce == 'T' and escolha_maq == 'Papel':
        print('Tesoura ' + 'x ' + escolha_maq + ' = Tesoura corta papel, você venceu.')
        num_vitoria += 1
    elif voce == 'P' and escolha_maq == 'Tesoura':
        print('Papel ' + 'x ' + escolha_maq + ' = Tesoura corta papel, você perdeu.')
        num_derrota += 1
    elif voce == 'R' and escolha_maq == 'Papel':
        print('Pedra ' + 'x ' + escolha_maq + ' = Papel embrulha pedra, você perdeu.')
        num_derrota += 1
    elif voce == 'T' and escolha_maq == 'Pedra':
        print('Tesoura ' + 'x ' + escolha_maq + ' = Pedra quebra tesoura, você perdeu.')
        num_derrota += 1
    
    print('\n##########################\n')

    print('Derrotas = ' + str(num_vitoria))
    print('Empate = ' + str(num_empate))
    print('Derrotas = ' + str(num_derrota))

    print('\n##########################\n')



