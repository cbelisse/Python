'''
Data: 13/03/2023
Autor: Cleber Belisse
Descrição: 1)	Faça um programa para adivinhar um número de 0 a 10000.
Se você errar o computador deverá responderse é mais ou menos.
Se você errar 10 vezes você perde o jogo.
'''

import random
number1 = random.randint(1, 10000)
print(number1)

chute = int(input('Digite um número'))
print(chute)
tentativas = 0

while tentativas < 10:
        tentativas += 1
        if chute < number1:
            print('Você escolheu um número menor do que o certo.')
            chute = int(input('Digite outro número'))
        elif chute > number1:
            print('Você escolheu um número maior do que o certo.')
            chute = int(input('Digite outro número'))
        else:
            print('Parabéns, você acertou o número.')

print('Acabaram suas chances!')




