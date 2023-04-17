'''
Data: 17/0/04/2023
Autor: Cleber Belisse
Descrição: Liberação de gratuidade no transporte público
Uma empresa de transporte público quer fazer um sistema automático para identificar se o usuário terá gratuidade no
transporte ou não.
Faça um programa que pergunte a idade do usuário, se ele tiver 65 anos ou mais irá informar que ele tem gratuidade
no transporte.
'''
titulo = 'Gratuidade no transporte público'
print('Seja bem vindo ao programa de' + titulo)
idade = int(input('Por favor, informe a sua idade: '))
if idade >= 65:
    print("Você tem direito a gratuidade no transporte público.")
else:
    print("Você ainda não tem direito a gratuidade no transporte público.")
print('Obrigado.')