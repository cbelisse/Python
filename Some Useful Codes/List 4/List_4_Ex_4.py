'''
Data: 28/04/2023
Autor: Cleber Belisse
Descrição: Validar se os dois dígitos do CPF são válidos
4)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se os dois dígitos
verificadores estão corretos (no caso do exemplo, o número 1 e número 0 após o traço).
Para validar o primeiro dígito, siga o exemplo executado no exercício 3.
Para validar o segundo dígito verificador deve seguir os seguintes passo:
1.	Multiplicar cada número por um valor respectivo+ o primeiro dígito verificador:
Ex: CPF 132.465.987-46
1      3      2      4      6      5      9      8      7       4
X
11   10     9      8      7      6      5      4     3        2
=
11    30   18     32   42    30    45    32     21     8
2.	Somar os resultados:
11 + 30 + 18 + 32 + 42 + 30 + 45 + 32 + 21 + 8 = 269
3.	Multiplicar o resultado por 10:
269 x 10 = 2690
4.	Obter o resto da divisão do valor por 11:
2690 % 11 = 6
5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 6)
6.	Se o Resultadofor igual ao segundo dígito verificador está correto, senão está incorreto
CPF  do exemplo: 132.465.987-46
2º Digito verificador: 6
Resultado do cálculo: 6
Logo:
CPF válido
'''
titulo = '"Valida CPF com os dois dígitos"'
print('Bem vindo ao programa: ' + titulo)
cpf = input("Digite seu cpf:")
cpfnumeros = cpf.replace('.','')
cpfnumeros= cpfnumeros.replace('-','')
#print(cpfnumeros)
listanumeros = []
multiplicador = 11
somatotal = 0

if len(cpf) != 14:
    print("CPF inválido")
else:
    for valor in cpfnumeros[:9]:
        multiplicador -= 1
        listanumeros.append(int(valor)*multiplicador)
    #print(listanumeros)

    for dig in cpfnumeros[-2:]:
        listanumeros.append(int(dig))
    #print(listanumeros)

    for soma in listanumeros[:9]:
        somatotal += soma*10

    #print(somatotal)

    restopor11 = somatotal%11

    if restopor11 > 9:
        digito = 0
    else:
        digito = restopor11
    print()
    print("O primeiro digito do cpf deve ser: " + str(digito))

    digito1 = "APROVADO"
    if listanumeros[-2] != digito:
        print("CPF inválido")
        digito1 = "REPROVADO"
    else:
        print('Primeiro dígito verificador está APROVADO')
    print()
    ''' Válidando o Segundo Dígito'''
    if digito1 == "APROVADO":
        listanumeros2 = []
        multiplicador2 = 12
        somatotal2 = 0

        for valores2 in cpfnumeros[:10]:
            multiplicador2 -= 1
            listanumeros2.append(int(valores2)*multiplicador2)

        #print(listanumeros2)

        for soma2 in listanumeros2[:10]:
            somatotal2 += soma2*10
        #print(somatotal2)

        restopor11_2 = somatotal2%11

        if restopor11_2 > 9:
            segundodigito = 0
        else:
            segundodigito = restopor11_2

        print("O segundo dígito deve ser: " + str(segundodigito))

        digito2 = "APROVADO"
        if listanumeros[-1] != segundodigito:
            print("Segundo dígito: APROVADO.")
            digito2 = "REPROVADO"
        else:
            print("Segundo dígito válido.")
        print()
        if digito1 == "APROVADO" and digito2 == "APROVADO":
            print("CPF VÁLIDO")
        else:
            print("CPF REPROVADO")
