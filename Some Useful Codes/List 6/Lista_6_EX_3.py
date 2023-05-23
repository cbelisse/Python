titulo = 'Lista de alunos'
'''
Data: 20/05/2023
Autor: Cleber
Descrição: Tira a média dos alunos 
de um arquivo txt e retorna como CSV
'''
print('Bem vindo ao programa ' + titulo + '\n')

import csv

lista_alunos = []

with open('Arquivos/alunos.txt','r') as file:
    linhas = file.read().split('\n')
    for linha in linhas:
        coluna = linha.split(',')
        media = (float(coluna[1]) + float(coluna[2])) / 2
        aluno = []
        aluno.append(coluna[0])
        aluno.append(coluna[1])
        aluno.append(coluna[2])
        aluno.append(media)
        lista_alunos.append(aluno)


with open('Arquivos/alunos.csv','w',newline='') as file:
    writer = csv.writer(file)
    header = ['Nome', 'Nota 1', 'Nota 2', 'Média']
    writer.writerow(header)
    for aluno in lista_alunos:
        writer.writerow(aluno)