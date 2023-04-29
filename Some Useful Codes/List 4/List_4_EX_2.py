'''
Duvidas:
1) Não consigo usar variável para indicar índice nos métodos ?
'''

'''
Data 22/04/23
Autor: Cleber Belisse
Descrição:  Trabalhando com conjunto de dados e métodos.

Crie um programa para inserir, apagar e listar os itens de uma lista de compras (utilize append e pop/del).
'''
titulo =  '"Trabalhando com conjunto de dados e métodos."'
print("Bem vindo ao programa " + titulo)
lista_compras = ["Arroz","Feijão","Batata","Marcarrão","Bife","'Zoião'"]
print("A lista de compras atual é: ")
for indice in range(len(lista_compras)):
    print(str(indice+1) + ': ' + str(lista_compras[indice]))
print()

adicionar = "S"
while adicionar == "S":
    adicionar = input("Deseja adionar mais algum item ? Digite: S para sim e N para não.").upper()
    if adicionar == "S":
        lista_compras.append(input("Qual item adicionar a lista?"))
        for indice in range(len(lista_compras)):
            print(str(indice + 1) + ': ' + str(lista_compras[indice]))
    else:
        print("Sua lista permanece inalterada.")

print()
remover = "S"
while remover == "S":
    remover = input("Deseja remover algum item ? \nDigite S para sim ou N para não.").lower()
    if remover == "s":
        numitemdeletar = int(input("Qual o número do item que deseja deletar ?"))
        lista_compras.pop(numitemdeletar-1)
    else:
        print("Sua lista permanece inalterada")

print(lista_compras)


