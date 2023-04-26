'''
Data: 25/03/2023
Autor: Cleber Belisse
Descrição: Caulculando aumento salarial (Calculating salary increase)
Este programa calcula o aumento no salário conforme faixa salarial ( This program calculates the percentage of increase in salary according to salary range).
• Salary up to $1,499.00  increase of 25%
• Salary Between R$1,500.00 and R$1,999.99 Increase of 20%
• Salary Between R$2,000.00 and R$2,999.99  Increase of 15%
• Salary Between R$3,000.00 and R$4,999.99  increase of 10% 
• Salary greater than BRL 5,000.00  5% increase

Uma empresa pretende fazer um reajuste salarial para os funcionários e precisa da sua ajuda para criar um programa.
Ficou definido os ajustes confome lista acima.

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



