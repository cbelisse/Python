'''
Data 13/05/2023
Autor: Cleber
6)	Crie uma função que receba o nome e idade e então cadastre como um dicionário (dict) em uma lista de usuários.
'''
titulo = 'Cadastro Usuário'
lista_usuarios = []

def cadastrar_usuario(nome,idade):
    usuario = {}
    usuario['nome'] = nome
    usuario['idade'] = idade
    lista_usuarios.append(usuario)

cadastrar_usuario('Daniel',29)

nome_1 = input('Digite um nome: ')
idade_1 = int(input("Digite a idade: "))

cadastrar_usuario(nome_1,idade_1)

print(lista_usuarios)

for usuario in lista_usuarios:
    print(usuario)

    for key, value in usuario.items():
        print(key,':',value)
    print("--------------------------------")