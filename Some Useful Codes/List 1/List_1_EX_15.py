titulo = 'Calculadora de média'
'''
Data: 05/03/2023
Autor: Cleber Belisse
Descrição: Calcula a média de duas notas
'''
'''
15)	Uma professora gostaria um programa para 
auxiliá-la a montar a média final de seus alunos. Sabendo que são 2 notas por semestre, monte um programa que
através das notas informadas pelo usuário mostre a sua média final. Não esqueça de manter uma boa interface 
com o usuário!!
'''
print('Seja bem vindo ao programa ' + titulo)

print('Por favor, informe a primeira nota')
nota1 = float(input())

print('Informe a segunda nota')
nota2 = float(input())

media = (nota1 + nota2) / 2

print('Sua média é ' + str(media))