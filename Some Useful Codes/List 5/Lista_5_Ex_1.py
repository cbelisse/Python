'''
Data 06/05/2023
Autor: Cleber
'''

def recebenome(nome):
    nome4letras = nome[:4]
    nomemon = nome4letras + "mon"
    return nomemon

digitado=input("Digite seu nome: ")

nomedigitado = recebenome(digitado)

print(nomedigitado)





