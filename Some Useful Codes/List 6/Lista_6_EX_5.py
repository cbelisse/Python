titulo = 'Macro teclado'
'''
Data: 20/05/2023
Autor: Cleber
Descrição: Cria uma macro de teclado
ativada pelo botão do meio do mouse
'''
print('Bem vindo ao programa ' + titulo + '\n')
import keyboard
import mouse
import time

while True:
    if mouse.is_pressed('middle'):
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')
