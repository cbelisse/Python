titulo = 'Criptografador de Texto'
'''
Data: 09/05/2023
Autor: Cleber
Descrição: Criptograma um texto informado pelo usuario
deslocando cada palavra 3 letras para direita
'''
print('Bem vindo ao programa ' + titulo + '\n')

def criptografia(_texto, desloc = 3):
    lista_texto = _texto.split(' ')
    texto_alterado = ''
    for palavra in lista_texto:
        if len(palavra) >= desloc:
            texto_alterado += (palavra[-desloc:] + palavra[:-desloc])
        else:
            for indice,letra in enumerate(palavra):
                indice_alterado = indice + desloc
                while indice_alterado > (len(palavra)-1):
                    indice_alterado -= len(palavra)
                texto_alterado += palavra[indice_alterado]
        texto_alterado += ' '
    return texto_alterado



texto = input('Digite um texto: ')
desloc = int(input('Digite o deslocamento: '))
print(criptografia(texto))

print(criptografia(texto,desloc))