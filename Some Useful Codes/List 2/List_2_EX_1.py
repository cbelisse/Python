'''
Data: 17/04/2023
Título: identificar se o número é par ou ímpoar.
Autor: Cleber Belisse
Descrição: Neste programa o usuário insere um número e o código identifica se o número é par ou ímpar
(In this program the user enters a number and the code identifies whether the number is even or odd).
'''
Faça um programa que peça um número ao usuário e informe se é Par ou Ímpar
titulo = "Identificador de números"
print('Seja bem vindo ao programa ' + titulo)
numero = int(input('Por favor, digite um número:'))
resto = numero % 2 > 0
if resto == 0:
    print('O número ' + str(numero) + ' é par.')
else:
    print('O número ' + str(numero) + ' é ímpar.')