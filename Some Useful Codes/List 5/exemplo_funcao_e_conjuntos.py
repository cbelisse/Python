
nome = 'Batata'

print(nome[:5])
'''

def funcao_soma(numero_1, numero_2):
    soma = numero_1 + numero_2
    print(soma)
    return soma



def idade_mais_10(idade):
    try:
        idade = int(idade)
        idade += 10
        print(idade)
        return True
    except:
        return False


#soma_1 = funcao_soma(1,2)
#soma_2 = funcao_soma(10,20)
#funcao_soma(soma_1,soma_2)

idade_1 = input('Digite a idade: ')

if idade_mais_10(idade_1):
    print('continuando programa')