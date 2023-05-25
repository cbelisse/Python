titulo = 'Lista de compras'
'''
Data: 20/05/2023
Autor: Cleber
Descrição: Faz uma lista de compras
com a possibilidade de gravar a lista em um arquivo
'''
print('Bem vindo ao programa ' + titulo + '\n')

import csv

nome = input('Digite seu nome: ').upper()
arquivo = 'Arquivos/compras_'+ nome + '.csv'

def listar_itens():
    if len(lista_de_compras) > 0:
        print('\nLista de Compras:')
        for produto in lista_de_compras:
            item, quantidade = produto
            print(quantidade, item, sep=': ')
    else:
        print('Não tem produtos nesta lista')
lista_de_compras = []

try:
    with open(arquivo,'r') as file:
        reader = csv.reader(file)
        for linha in reader:
            lista_de_compras.append(linha)
        print('Lista de Compras Carregada pro sistema')
except:
    print('Criando nova lista de compras')

while True:
    print('''
Escolha uma opção
(I) --> Inserir item
(D) --> Deletar item
(L) --> Exibir lista de compras
(S) --> Salvar lista em arquivo
(X) --> Finalizar programa''')

    escolha = input('Escolha: ').upper()

    if escolha == 'I':
        item = input('Digite o nome do produto: ').upper()
        quantidade = input('Digite a quantidade: ')
        if len(item) > 0 and quantidade.isdecimal():
            if int(quantidade) > 0:
                existe = False
                for produto in lista_de_compras:
                    item_lista ,quantidade_lista = produto
                    if item_lista == item:
                        existe = True
                        break
                if existe == False:
                    produto = []
                    produto.append(item)
                    produto.append(quantidade)
                    lista_de_compras.append(produto)
                    print('Produto inserido com sucesso')
                else:
                    print('Item já existe na lista')
            else:
                print('Quantidade inválida')
        else:
            print('Erro ao inserir produto')
    elif escolha == 'D':
        listar_itens()
        deletar = input('Digite o item a ser deletado: ').upper()
        deletou = False
        for produto in lista_de_compras:
            item,quantidade = produto
            if item == deletar:
                deletou = True
                lista_de_compras.remove(produto)
                break
        if deletou == True:
            print('Item deletado com sucesso')
        else:
            print('Item não encontrado')
    elif escolha == 'L':
        listar_itens()
    elif escolha == 'S':
        with open(arquivo,'w',newline='') as file:
            writer = csv.writer(file)
            for produto in lista_de_compras:
                writer.writerow(produto)
        print('Lista de Compras Salva')
    elif escolha == 'X':
        print('Encerrando o programa')
        break
    else:
        print('Opção inválida')