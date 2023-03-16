'''
Data: 13/03/2023
Autor: Cleber Belisse
Descrição: Idetificar se o um é Bissexto ou não
Leia o texto abaixo sobre o Ano Bissexto:
“O calendário gregoriano, estabelecido pela primeira vez em 1582 pelo Papa Gregório XIII,
foi projetado para corrigir os erros introduzidos pelo calendário juliano, que é menos preciso.

No calendário gregoriano, um ano normal consiste em 365 dias. Como o comprimento real de um ano sideral
(o tempo necessário para a Terra girar uma vez sobre o Sol) é na verdade de 365,2425 dias, um "ano bissexto" de 366 dias é usado uma vez a cada quatro anos para eliminar o erro causado por três anos normais (mas curtos). Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.

No entanto, ainda há um pequeno erro que deve ser contabilizado. Para eliminar esse erro,
o calendário gregoriano estipula que um ano que é uniformemente divisível por 100 (por exemplo, 1900) é um ano bissexto apenas se também é igualmente divisível por 400.

Por essa razão, os seguintes anos não são bissextos: 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
Isso porque eles são uniformemente divisíveis por 100, mas não por 400.
Os seguintes anos são bissextos: 1600, 2000, 2400
Isso porque eles são uniformemente divisíveis por 100 e 400.”
Faça um programa no qual o usuário informe um anoe o sistema responda se o ano é bissexto ou não.

'''
titulo = 'Identificador de ano Bissexto verdadeiro'
print('Bem vindo ao programa ' + titulo)
print('Por favor, insira o ano que deseja verificar')
ano = int(input())
bissexto_simples = ano % 4
bissexto_por_100 = ano % 100
bissexto_por_400 = ano % 400

if bissexto_simples == 0 and bissexto_por_100 == 0 and bissexto_por_400 == 0:
    print(str(ano) + ' é um ano bissexto verdadeiro')
elif bissexto_simples == 0 and bissexto_por_100 != 0:
    print(str(ano) + ' é um ano bissexto simples')
else:
    print(str(ano) + ' não é um ano bissexto.')

#Ano bissexto simples divide por 4 e não é uniformemente divivel por 100.
