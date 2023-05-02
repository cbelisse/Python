'''
Data: 13/03/2023
Autor: Cleber Belisse
Descrição: Pragrama para liberar a menor quantidade de cédulas de dinheiro no momento do saque.
8)	Faça um programa de um caixa eletrônico que, a partir do valor a ser sacado informado pelo usuário,
o programa informe a menor quantidade de cédulas que o usuário irá receber, informando-o quantas cédulas
e de quais valores ele irá receber.
Considerar apenas notas:
R$200,00
R$100,00
R$50,00
R$20,00
R$10,00
R$5,00
R$2,00
R$1,00

Exemplo:
R$ 858,00
O programa irá informar:
Cédulas de 200 reais: 4
Cédulas de 50 reais: 1
Cédulas de 5 reais: 1
Cédulas de 2 reais: 1
Cédulas de 1 real: 1

'''
titulo = 'Liberando a menor quantidade de cédulas'
print('Bem vindo ao programa' + titulo)
valor = int(input('Insira o valor a ser liberado: '))

resto_200 = valor % 200
resto_100 = resto_200 % 100
resto_50 = resto_100 % 50
resto_5 = resto_50 % 5
resto_2 = resto_5 % 2

if resto_200 == 0:
    cedulas_de_200 = valor // 200
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200.')
elif resto_200 != 0 and resto_100 == 0:
    cedulas_de_200 = valor // 200
    cedulas_de_100 = resto_200 // 100
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200\n' + str(cedulas_de_100) + ' cédula(s) de R$ 100.')
elif resto_200 != 0 and resto_100 != 0 and resto_50 == 0:
    cedulas_de_200 = valor // 200
    cedulas_de_100 = resto_200 // 100
    cedulas_de_50 = resto_100 // 50
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200\n' + str(cedulas_de_100) + ' cédula(s) de R$ 100\n' +
    str(cedulas_de_50) + ' cédula(s) de R$ 50.')
elif resto_200 != 0 and resto_100 != 0 and resto_50 != 0 and resto_5 == 0:
    cedulas_de_200 = valor // 200
    cedulas_de_100 = resto_200 // 100
    cedulas_de_50 = resto_100 // 50
    cedulas_de_5 = resto_50 // 5
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200\n' + str(cedulas_de_100) +
          ' cédula(s) de R$ 100\n' + str(cedulas_de_50) + ' cédula(s) de R$ 50\n' + str(cedulas_de_5) +
          ' cédula(s) de R$ 5.')

elif resto_200 != 0 and resto_100 != 0 and resto_50 != 0 and resto_5 != 0 and  resto_2 == 0:
    cedulas_de_200 = valor // 200
    cedulas_de_100 = resto_200 // 100
    cedulas_de_50 = resto_100 // 50
    cedulas_de_5 = resto_50 // 5
    cedulas_de_2 = resto_5 // 2
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200\n' + str(cedulas_de_100) +
          ' cédula(s) de R$ 100\n' + str(cedulas_de_50) + ' cédula(s) de R$ 50\n' + str(cedulas_de_5) +
          ' cédula(s) de R$ 5\n' + str(cedulas_de_2) + ' cédula(s) de R$ 2')
else:
    cedulas_de_200 = valor // 200
    cedulas_de_100 = resto_200 // 100
    cedulas_de_50 = resto_100 // 50
    cedulas_de_5 = resto_50 // 5
    cedulas_de_2 = resto_5 // 2
    cedulas_de_1 = resto_2 // 1
    print('Você receberá:\n' + str(cedulas_de_200) + ' cédula(s) de R$ 200\n' + str(cedulas_de_100) +
          ' cédula(s) de R$ 100\n' + str(cedulas_de_50) + ' cédula(s) de R$ 50\n' + str(cedulas_de_5) +
          ' cédula(s) de R$ 5\n' + str(cedulas_de_2) + ' cédula(s) de R$ 2\n' + str(cedulas_de_1) + ' cédula(s) de R$ 1')