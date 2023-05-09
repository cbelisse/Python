titulo = 'Inversor de texto'
'''
Data: 06/05/2023
Autor: Cleber
Descrição: Inverte um texto
'''

def inverte_texto(texto):
    texto_invertido = ''
    for indice in range(-1, -len(texto) - 1, -1):
        texto_invertido += texto[indice]
    return texto_invertido

print('Digite um texto:')
texto1 = input()

print(inverte_texto(texto1))

print(inverte_texto('Aula de Python'))