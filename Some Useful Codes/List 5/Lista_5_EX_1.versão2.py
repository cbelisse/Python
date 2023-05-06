titulo = 'Digimon'
'''
Data: 06/05/2023
Autor: Cleber
Descrição: Transforma um nome em digimon
'''
print('Seja bem vindo ao programa ' + titulo)

def conversor_mon(_nome):
    nomemon = _nome[:4] + 'mon'
    print(nomemon)

print('Por favor digite um nome')
nome = input()
conversor_mon(nome)