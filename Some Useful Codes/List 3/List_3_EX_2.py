'''
Data: 25/03/2023
Autor: Cleber Belisse
Descrição:
2)	Faça um programa para avaliar qual o número que mais cai em um lance de dois dados (D6).
O sistema deverá lançar um conjunto de dois dados n vezes seguidas, onde n é o número de vezes que você informar ao computador.
Após jogar os dados, o sistema deverá informar quantas vezes a soma deu cada um dos números possíveis: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12.

'''
import random as rd
titulo = '"ANALISANDO O JOGO DE DOIS DADOS"'
print('Bem vindo ao programa ' + titulo)

num_rodadas = int(input('Quantas rodas você deseja jogar os dois dados ?'))

resultado2 = 0
resultado3 = 0
resultado4 = 0
resultado5 = 0
resultado6 = 0
resultado7 = 0
resultado8 = 0
resultado9 = 0
resultado10 = 0
resultado11 = 0
resultado12 = 0



#Vai até a jogada 5
for jogada in range(num_rodadas):
    dado1 = rd.randint(1,6)
    dado2 = rd.randint(1,6)

    somadados = dado1 + dado2

    print('Estamos na jogada de número ' + str(jogada))
    if somadados == 2:
        resultado2 += 1
    elif somadados == 3:
        resultado3 += 1
    elif somadados == 4:
        resultado4 += 1
    elif somadados == 5:
        resultado5 += 1
    elif somadados == 6:
        resultado6 += 1
    elif somadados == 7:
        resultado7 += 1
    elif somadados == 8:
        resultado8 += 1
    elif somadados == 9:
        resultado9 += 1
    elif somadados == 10:
        resultado10 += 1
    elif somadados == 11:
        resultado11 += 1
    elif somadados == 12:
        resultado12 += 1

print('Soma 2: ' + str(resultado2))
print('Soma 3: ' + str(resultado3))   
print('Soma 4: ' + str(resultado4))   
print('Soma 5: ' + str(resultado5))   
print('Soma 6: ' + str(resultado6))   
print('Soma 7: ' + str(resultado7))   
print('Soma 8: ' + str(resultado8))   
print('Soma 9: ' + str(resultado9))   
print('Soma 10: ' + str(resultado10))   
print('Soma 11: ' + str(resultado12))   



    


