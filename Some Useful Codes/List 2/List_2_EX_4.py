'''
Data: 06/03/2023
Autor: Cleber Belisse
Descrição: Calcula desconto com base na idade (Calculates discount based on age)
O cliente insere a idade no programa e o código calcula o percentual de desconto sobre o produto de acordo com a idade
do cliente. No final o sistema informa o preço inicial e o preço final com desconto.

(The customer enters the age in the program and the code calculates the percentage of discount on the product according
to the age of the customer. At the end the system informs the initial price and the final price at a discount).

Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que custa R$200,00.
O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto máximo será de 80%.
Faça um programa que pergunte a idade do usuário e então mostre o valor final do óculos e o desconto adquirido.
'''

titulo = 'Cálculo de desconto'
print('Seja Bem vindo ao programa ' + titulo)
idade = int(input('Digite sua idade para receber o desconto: '))
valor_inicial = 200
desconto = idade

if desconto > 80:
    desconto = 80
elif desconto < 10:
    desconto = 10

valor_desconto = valor_inicial * desconto / 100
valor_final = valor_inicial -  valor_desconto
print('Você recebeu um desconto de ' + str(desconto) + '% e o óculos custará ' + str(valor_final))

