# Jogo par ou impar

# Importação das bibliotecas
import random as rd
import time

# Criação das variáveis globais
num_vit = 0
num_der = 0

# Loop do Jogo
while True:
    # Escolha inicial Par ou Impar
    print('Escolha par (P) ou impar (I), para sair digite (Q)')
    escolha = input()
    
    if escolha != 'P' and escolha != 'I' and escolha != 'Q':
        print('Você digitou um comando inválido')
        continue
    # Caso digite Q o jogo é finalizado
    if escolha == 'Q':
        print('Jogo Finalizado')
        time.sleep(1)
        print('\nNúmero de Vitórias: ' + str(num_vit))
        print('Número de Derrotas: ' + str(num_der) + '\n')
        time.sleep(2)
        break
    
    # Número do jogador
    print('\nEscolha um numero de 0 a 9')
    jogador_num = int(input())
    print('\nVocê jogou ' + str(jogador_num))
    time.sleep(1)
    
    # Número do PC
    pc_num = rd.randint(0,9)
    print('\nO PC jogou ' + str(pc_num))
    time.sleep(1)
    
    # Soma dos números
    soma = jogador_num + pc_num
    print('\nA soma é ' + str(soma))
    time.sleep(2)
    
    # Determinação de quem venceu ou perdeu
    if escolha == 'P':
        if soma % 2 == 0:
            print('\nVocê venceu!')
            num_vit = num_vit + 1
        else:
            print('\nVoce perdeu!')
            num_der = num_der + 1
    elif escolha == 'I':
        if soma % 2 == 0:
            print('\nVoce perdeu!')
            num_der = num_der + 1
        else:
            print('\nVocê venceu!')
            num_vit = num_vit + 1
    else:
        print('\nVocê não escolheu nem par (P) nem impar (I)')
    
    # Print do número de vitorias e derrotas atuais
    time.sleep(1)
    print('\nNúmero de Vitórias: ' + str(num_vit))
    print('Número de Derrotas: ' + str(num_der) + '\n')
    time.sleep(2)
    # Reinicia o ciclo


