print('Quanto é 2 + 2')
resposta = int(input())
tentativas = 4

while resposta != 4:
    tentativas -= 1
    print('Errrrrrooooou')
    if tentativas == 0:
            tentativas = 4
            print('Aguarde 5s para tentar novamente')
            time.sleep(5)

    print('Quanto é 2+2 ?')
    resposta = int(input())
else:
    print('Certa a resposta')
    
        
    