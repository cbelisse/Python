titulo = 'Criptografia padrão 2'
'''
Data: 08/05/05/2023
Autor: Cleber
Descrição: Criptografa um texto padrão 2.
5)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
Faça o deslocamento de 3 letras para direita por palavra

Exemplo: Usuário digitou “Aula de Python”
Sistema retornou “ulaAedhonPyt”

Aula de Python --> ulaA ed honPyt
'''
print('Seja bem vindo ao programa ' + titulo)

def criptografa_texto(texto):
    lista = texto.split(' ')
    texto_crip = ''
    for palavra in lista:
        if len(palavra) >= 4:
            texto_crip += palavra[-3:] + palavra[:-3]
        elif len(palavra) == 2:
            texto_crip += palavra[-1] + palavra[0]
        else:
            texto_crip += palavra
        texto_crip += ' '
    return texto_crip

print('Digite um texto:')
texto1 = input()

print(criptografa_texto(texto1))