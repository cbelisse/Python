'''
Data: 06/03/2023
Autor: Cleber Belisse
Descrição: Avaliando desempenho de alunos
    Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
•	Aprovado  Acima de 7
•	Reprovado  Abaixo de 5
•	Recuperação  Entre 5 e 7
'''
titulo = 'Avaliação de desempenho de alunos'
print('Seja bem vindo ao programa ' + titulo)
matematica = float(input('Por favor, informe a nota em matemática: '))
portugues = float(input("Informe a note em Português: "))
media = (matematica + portugues) / 2
if media > 7:
    print('A média do aluno é ' + str(media) + ', portanto, ele está aprovado.')
elif media < 5:
    print("A média do aluno é " + str(media) + ', portanto, ele está reprovado')
else:
    print("A média do aluno é " + str(media) + ', portanto, ele está de recuperação')