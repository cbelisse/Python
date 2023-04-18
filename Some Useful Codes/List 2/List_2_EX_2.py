'''
Data: 17/04/2023
Autor: Cleber Belisse
Descrição: Gratuidade na passagem do transporte público para idosos (Free public transport tickets for the elderly)
O usuário insere a sua idade e o programa verifica se ele tem direito a gratuidade na passagem do transporte público
(The user enters his age and the program verified if he is entitled to free public transport ticket).

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