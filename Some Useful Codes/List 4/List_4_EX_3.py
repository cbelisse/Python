'''
Data: 28/04/2023
Autor: Cleber Belisse
Descrição: Validando se o primeiro dígito do CPF está correto
3)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se o primeiro digito verificador está correto (no caso do exemplo, o número 1 após o traço).
Para validar este dígito verificador deve seguir os seguintes passo:
1.	Multiplicar cada número do CPF por um valor respectivo:
Ex: CPF 132.465.987-10

1   32  4   659      8  7
X
10 9    8    7    6    5    4    3    2
=
10   27    16    28    36     25   36    24    14

2.	Somar os resultados:

10 + 27 + 16 + 28 + 36 + 25 + 36 + 24 + 14 = 216

3.	Multiplicar o resultado por 10:

216 x 10 = 2160

4.	Obter o resto da divisão do valor por 11:

2160 % 11 = 4

5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 4)

6.	Se o Resultadofor igual ao primeiro dígito verificador está correto, senão está incorreto
CPF  do exemplo: 132.465.987-10
1º Digito verificador: 1
Resultado do cálculo: 4
Logo:
CPF inválido

'''
titulo = '"Validando Primeiro Dígito do CPF"'
print('Bem vindo ao programa: ' + titulo)
cpf = input("Digite seu cpf:")
cpfnumeros = cpf.replace('.','')
cpfnumeros= cpfnumeros.replace('-','')
print(cpfnumeros)
listanumeros = []
multiplicador = 11
somatotal = 0

if len(cpf) != 14:
    print("CPF Inválido")
else:
    for valor in cpfnumeros[:9]:
        multiplicador -= 1
        listanumeros.append(int(valor)*multiplicador)
        print(valor,' x ', multiplicador)
    print(listanumeros)

    for dig in cpfnumeros[-2:]:
        listanumeros.append(int(dig))
    print(listanumeros)

    for soma in listanumeros[:9]:
        somatotal += soma*10

    print(somatotal)

    restopor11 = somatotal%11

    if restopor11 > 9:
        digito = 0
    else:
        digito = restopor11

    print("O primeiro digito do cpf deve ser: " + str(digito))

    if listanumeros[-2] != digito:
        print('Primeiro dígito verificador REPROVADO')
    else:
        print("Até o primeiro dígito APROVADO")
