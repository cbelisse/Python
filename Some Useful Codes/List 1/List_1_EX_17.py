titulo = 'Calculadora de Latas de Tinta'
'''
Data: 05/03/2023
Autor: Cleber Belisse
Descrição: Calcula o imc e faz cadastro de usuário
'''
'''
17)	Um fabricante de tintas quer montar um programa que auxilie o comprador a saber quantas latas de tinta ele precisará para pintar sua parede. 
Monte um programa em python que execute esta função a partir dos dados informados pelo usuário (largura e altura), 
sabendo que cada lata de tinta cobre 3m² de parede. Não esqueça de manter uma boa interface com o usuário!!
'''
print('Seja bem vindo ao programa ' + titulo)

print('Por favor, informe a largura da parede')
largura = float(input())

print('Informe a altura da parede')
altura = float(input())

area = largura * altura
area_lata = 3

latas_inteiro = area // area_lata
latas_resto = area % area_lata
tem_resto = latas_resto > 0
latas_final = int(latas_inteiro + int(tem_resto))

'''
Lembre-se que int(True) vale 1 e int(False) vale 0
print('Area: ' + str(area))
print('Latas inteiro: ' + str(latas_inteiro))
print('Latas resto: ' + str(latas_resto))
print('Tem resto? ' + str(tem_resto))
print('Latas Final: ' + str(latas_final))
'''

print('Você precisará de pelo menos ' + str(latas_final) + ' latas de tinta')










