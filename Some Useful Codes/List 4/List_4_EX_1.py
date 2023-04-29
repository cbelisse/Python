'''
Data: 21/04/23
Autor: Cleber Belisse
Título: Trabalhando com conjuntos de dados.

Faça um programa para imprimir estes dados com os índices de cada um dos nomes abaixo
jose
jorge
maria
antonio
ana
julia
márcio
fernando
zelia

'''
titulo = '"Trabalhando com conjuntos de dados"'
print("Bem vindo ao programa " + titulo)
nomes = ['jose','jorge','maria','Antonio','ana','julia','márcio','fernando','zelia']

for indice in range(len(nomes)):
    print(str(indice+1) + ': ' + str(nomes[indice]))