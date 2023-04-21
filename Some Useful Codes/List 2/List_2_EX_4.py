'''
Data: 06/03/2023
Autor: Cleber Belisse
Descrição: Calcula desconto com base na idade (Calculates discount based on age)
O cliente insere a idade no programa e o código calcula o percentual de desconto sobre o produto. No final o sistema
informa o preço inicial e o preço final com desconto (The customer enters the age in the program and the code calculates
the discount percentage on the product. At the end the system informs the initial price and the final price at a discount).

Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que custa R$200,00.
O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto máximo será de 80%.
Faça um programa que pergunte a idade do usuário e então mostre o valor final do óculos e o desconto adquirido.
'''
titulo = 'Desconto com base na idade'
print('Seja bem vindo ao programa ' + titulo)
idade = int(input("Por favor, informe a sua idade para calcularmos o desconto: "))
valor_fixo = 200
percentual_a_pagar = (100 - idade) / 100
if idade <= 10:
    valor_com_desconto = valor_fixo * 0.90
    print("Você recebeu um desconto de 10%.")
    print('O óculos com desconto sairá por ' + str(valor_com_desconto))
elif idade >= 80:
    valor_com_desconto = valor_fixo * 0.20
    print("Você recebeu um desconto de 80%.")
    print('O óculos com desconto sairá por ' + str(valor_com_desconto))
else:
    valor_com_desconto = valor_fixo * percentual_a_pagar
    print("Você recebeu um desconto de " + str(idade) + '%')
    print('O óculos com desconto sairá por ' + str(valor_com_desconto))