nomes = ['Daniel', 'Jose', 'Maria', 'Andre']

def muda_nome(itens):
    if type(itens) == list:
        for item in itens:
            print(item[:4] + 'mon')
    elif type(itens) == str:
        print(itens[:4] + 'mon')

muda_nome(nomes)
muda_nome('Daniel')