'''
Data: 13/03/2023
Autor: Cleber Belisse
Descrição: Validando se a data realmente existe no calendário.

Faça um programa que pergunte uma data ao usuário (dia, mês e ano separadamente) e valide se aquela data é real ou não,
fazendo as seguintes validações:
•	Verificar se o dia informado existe dentro daquele mês
o	Tem 31 dias se o mês for 1, 3, 5, 7, 8, 10 ou 12;
o	Tem 30 dias se o mês for 4, 6, 9 ou 11;
o	Tem 28 dias se o mês for 2 e o ano não for bissexto;
o	Tem 29 dias se o mês for 2 e o ano for bissexto.
•	Verificar se o mês informado existe (ano vai até 12 meses);
•	Verificar se o dia, mês e ano são valores positivos.
Informar ao usuário se a data for válida ou não.
'''
titulo = '"Verificador de datas"'
print('Bem vindo ao programa ' + titulo)
dia = int(input('Por favor, digite um dia do mês: '))
mes = int(input('Digite o mês: '))
ano = int(input('E agora informe o ano, por favor: '))

ano_bissexto = ano % 4 == 0

if dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, pois este mês tem apenas 30 dias.')
elif dia > 31:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, confirme o dia informado.')
    ''' Verificar se o mês informado existe (ano vai até 12 meses.);'''
elif mes > 12:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, pois o mês informado não existe.')
    ''' Verificar se o dia, mês e ano são valores positivos.'''
elif dia <= 0 or mes <= 0 or ano <= 0:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, por favor, inserir apenas números positivos')
    '''
    o	Tem 28 dias se o mês for 2 e o ano não for bissexto;
    o	Tem 29 dias se o mês for 2 e o ano for bissexto.
    '''
elif ano_bissexto == False and mes == 2 and dia > 28: #Tem 28 dias se o mês for 2 e o ano não for bissexto;
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, pois este ano não é bissexto, portanto, Fevereiro tem apenas 28 dias.')
elif ano_bissexto == True and mes == 2 and dia > 29:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Data inválida, pois em ano bissexto igual a este, Fevereiro tem apenas 29 dias.')
else:
    print('Data: ' + str(dia) + '/' + str(mes) + '/' + str(ano))
    print('Esta é uma data válida.')