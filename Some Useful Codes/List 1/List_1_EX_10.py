'''
Titulo: Somador de numeros informados pelo usuario (Summing numbers reported by the user)
Data: 04/03/2023
Autor: Cleber Belisse
Descrição: Neste código o usuário insere dois números e o programa soma os dois.
(In this code the user enters two numbers and the program sums the two)
'''
# 10)	Monte um programa que exiba a soma de dois números inteiros informados pelo usuário.
print('Seja bem vindo ao programa Somador \
de numeros informados pelo usuario')

print('Por favor, informe o primeiro numero')
numero1 = int(input())

print('Informe o segundo numero')
numero2 = int(input())

resultado = numero1 + numero2

print('O resultado da sua soma será ' + str(resultado))