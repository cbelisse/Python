'''
Data: 07/03/2023
Autor: Cleber Belisse
Descrição: Calculando o reajuste salarial conforme salário.

Uma empresa pretende fazer um reajuste salarial para os funcionários e precisa da sua ajuda para criar um programa.
Ficou definido os seguintes reajustes:
•	Salário Abaixo de R$1.500,00  Aumento de 25%
•	Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
•	Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
•	Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
•	Salário Acima de R$5.000,00  Aumento de 5%

Faça um programa que pergunte ao usuário qual seu Salário Atual e mostre ao usuário:
1.	O salário atual;
2.	A porcentagem do reajuste;
3.	O aumento em R$;
4.	O salário final após o reajuste.
'''
titulo = 'Cálculo de reajuste salarial'
print('Seja bem vindo ao programada chamado '+ titulo)
print('Para calcular o reajuste, por favor, informe o salário atual.')
salario_atual = float(input('R$:'))

if salario_atual < 1500:
    aumento = 25
elif salario_atual < 2000:
    aumento = 20
elif salario_atual < 3000:
    aumento = 15
elif salario_atual < 5000:
    aumento = 10
else:
    aumento = 5

aumento_em_reais = salario_atual * aumento / 100
salario_final = salario_atual + aumento_em_reais
print('Seu salário atual é de R$' + str(salario_atual) + ', você receberá ' + str(aumento) +
      '% de aumento ou R$' + str(aumento_em_reais) +', então seu novo salário será R$ ' +str(salario_final) + '.')



