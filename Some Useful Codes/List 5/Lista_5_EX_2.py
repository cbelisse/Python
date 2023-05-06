titulo = 'Apelido'
'''
Data: 06/05/2023
Autor: Cleber
Descrição: Converte um nome completo
em um apelido com as 3 primeiras letras do
primeiro nome e as 3 ultimas letras do
ultimo nome
'''
print('Seja bem vindo ao programa ' + titulo)

def criador_de_apelidos(nome):
    apelido = nome[:3] + nome[-3:]
    print(apelido)

print('Por favor digite um nome completo')
nome_completo = input()

criador_de_apelidos(nome_completo)