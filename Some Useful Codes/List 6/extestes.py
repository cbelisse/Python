'''
Atenção para criar listas, pois os objetos devem estar entre colchetes, se colocar entre parenteses
você criará um Tuple e  se colocar entre chave criará sets.
'''

lista_linguagens=["CSS","JAVASCRIPT","HTML","PYTHON","JAVA"]
lista_preco=["R$100","R$200","R$300","R$400","R$500"]
lista_anolancamento=[2010,2012,2014,2016,2018]
lista_todos=[lista_linguagens,lista_preco,lista_anolancamento]
print(lista_todos)
print(lista_linguagens[3])
if "css" in lista_todos:
    print("Exite CSS na lista totos")
elif "css" in lista_anolancamento:
    print("Não tem CSS na lista todos, mas tem na lista anolancamento")
else:
    print("Não tem CSS em nenhuma das duas listas")

if "css" in lista_todos or lista_anolancamento or lista_linguagens:
    print("Existe CSS em uma das listas")
print()
for linguagens in lista_linguagens:
    print("Vamos falar destas linguagens: " + str(linguagens))
print()
for ordemlinguagens in range(len(lista_linguagens)):
    print(str(ordemlinguagens+1) + '-' + str(lista_linguagens[ordemlinguagens]))
print()
for indice,linguagem in enumerate(lista_linguagens,start=1):
    print(str(indice) + " - " + str(linguagem))

lista_linguagens.append('C++')
print(lista_linguagens)

lista_linguagens.pop(5)
print(lista_linguagens)