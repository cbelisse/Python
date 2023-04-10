'''
Titulo: Calculadora de quando terá 80 anos
Data: 05/03/2023
Autor: Cleber Belisse
Descrição: Calcula quando você terá 80 anos a partir
da idade informada
'''
'''
#14)	Faça um programa que mostre em que ano a pessoa terá 80
anos a partir da idade informada pelo usuário. Não esqueça de manter uma boa interface com o usuário!
'''
print('Seja bem vindo ao programa Calculadora de quando terá 80 anos')

print('Por favor, informe sua idade')
idade = int(input())

# ano_atual = 2023
print('Informe o ano atual')
ano_atual = int(input())
resultado = 80 - idade + ano_atual

print('Você terá 80 anos em ' + str(resultado))
