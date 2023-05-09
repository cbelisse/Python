'''
Data 06/05/2023
Autor: Cleber
3)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
Letra A  4
Letra B  8
Letra E  3
Letra I  1
Letra O  0
Letra T  7

Exemplo: Usuário digitou “Aula de Python”
Sistema retornou “4ul4 d3 Py7h0n

'''
titulo = '"Alterando texto."'
print("Bem vindo ao programa " + titulo)
texto = input('Digite um texto para ser codificado:').upper()

def criptografando(teste):
    teste = texto.replace("A","4")
    teste = teste.replace("B","8")
    teste = teste.replace("E","3")
    teste = teste.replace("I","1")
    teste = teste.replace("O","0")
    teste = teste.replace("T","7")
    return teste

teste = criptografando(texto)

print(teste)
