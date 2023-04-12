titulo = 'Calculadora de IMC'
'''
Data: 05/03/2023
Autor: Cleber Belisse
Descrição: Calcula o imc e faz cadastro de usuário
'''
'''
16)	Faça um programa que realize o cadastro de um usuário a partir de seu nome, idade, peso, altura que deverão ser 
informados pelo usuário e exiba a frase: Seu nome é ______ e tem ___ caracteres, você tem ___ anos e nasceu no ano de __.
Você mede _____cm, pesa ____ Kg e seu IMC é:____. Não esqueça de manter uma boa interface com o usuário!! 

*Fórmula do cálculo do IMC: IMC = Peso ÷ (Altura × Altura)
'''
print('Seja bem vindo ao programa ' + titulo)

print('Por favor, informe seu nome')
nome = input()
print('Informe sua idade')
idade = int(input())
print('Informe seu peso em Kg')
peso = float(input())
print('Informe seu altura em metros')
altura = float(input())

num_caracteres = len(nome)

ano_nascimento = 2023 - idade

altura_em_cm = int(altura * 100)

imc = peso / (altura * altura)

print('Seu nome é ' + nome + ' e tem ' + str(num_caracteres) + ' caracteres, você tem ' + str(idade) +
' anos e nasceu no ano de ' + str(ano_nascimento) + '. Você mede ' + str(altura_em_cm) + ' cm, pesa ' + str(peso) +
' Kg e seu IMC é: ' + str(imc) + '.')

#Nota: até o momento não aprendemos a limitar o n° de casas decimais.