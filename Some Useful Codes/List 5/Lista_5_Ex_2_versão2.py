'''
Data 06/05/2023
Autor: Cleber
Crie uma função que um nome completo, a função irá criar um codinome que irá utilizar as
3 primeiras letras de cada nome.
Ex: Sociedade Esportiva Palmeiras  SocEspPal

'''
nomecompleto = input("Digite seu nome completo: ")
listanome = nomecompleto.split(' ')
print(listanome)

def alterandonome(n):
    nova = ''
    for i in listanome:
        nova += i[:3]
    return nova

teste = alterandonome(nomecompleto)

print(teste)
