import time

titulo = 'Forca'
'''
Data: 15/04/2023
Autor: Cleber
Descrição: Jogo da Forca
Crie um programa de forca onde são disponibilizadas 10 tentativas para o seu oponente acertar a 
palavra.
'''

print('' * 10)

print('Seja bem vindo ao programa ' + titulo + '\n')

time.sleep(1)

palavra_secreta = input('Digite a palavra secreta: ').upper()

dica = input('Digite a dica para esta palavra: ')

print('\n' * 30)

palavra_descoberta = ''

for letra in palavra_secreta:
      if letra.isalnum():
            palavra_descoberta += '_'
      else:
            palavra_descoberta += letra


print('Descubra a palavra secreta')
time.sleep(1)
print('Dica: ' + dica)
time.sleep(1)
print('Palavra: ' + palavra_descoberta)
time.sleep(1)
print('\n\n')

tentativa = 1
letras_digitadas = ''

while True:
      print('\n##############################\n')
      time.sleep(0.5)
      print('Tentativa :' + str(tentativa) + '\n')
      time.sleep(0.5)
      print('Palavra: ' + palavra_descoberta + '\n')
      time.sleep(0.5)
      letra_tentativa = input('Digite uma letra: ').upper()
      time.sleep(0.5)
      if len(letra_tentativa) > 1:
            print('\nDigite apenas 1 letra')
            continue
      if not letra_tentativa.isalnum():
            print('\nDigite uma letra ou número')
            continue
      if letra_tentativa in letras_digitadas:
            print('\nVocê já digitou esta letra')
            time.sleep(0.5)
            print('Letras digitadas:')
            time.sleep(0.5)
            for letra in letras_digitadas:
                  print(letra + ', ', end= '')
            time.sleep(0.5)
            print('\nTente novamente')
            continue

      letras_digitadas += letra_tentativa
      palavra_temporaria = ''
      encontrou_letra = False
      for indice, letra in enumerate(palavra_secreta):
            if letra_tentativa == letra:
                  encontrou_letra = True
                  palavra_temporaria += letra
            else:
                  if letra in palavra_descoberta:
                        palavra_temporaria += letra
                  else:
                        palavra_temporaria += '_'
      
      if encontrou_letra == True:
            palavra_descoberta = palavra_temporaria
      else:
            time.sleep(0.5)
            print('\nERROUUUUUUUUUU')
            tentativa += 1
      
      if palavra_descoberta == palavra_secreta:
            time.sleep(0.5)
            print('\nPalavra: ' + palavra_secreta)
            time.sleep(0.5)
            print('Parabéns, Você venceu')
            break

      if tentativa > 10:
            time.sleep(0.5)
            print('\nPerdeu o jogo')
            time.sleep(0.5)
            print('A palavra era ' + palavra_secreta)
            break

      time.sleep(0.5)