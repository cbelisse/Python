titulo = 'Desenha com mouse'
'''
Data: 13/05/2023
Autor: Daniel
Descrição: Desenha a primeira letra
do seu nome ao clicar CTRL
'''
print('Bem vindo ao programa ' + titulo + '\n')

import mouse
import keyboard

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'ctrl':
            mouse.drag(0, 0, 0, 200, absolute=False, duration=0.2)
            mouse.drag(0, 0, 50, -50, absolute=False, duration=0.2)
            mouse.drag(0, 0, 25, -50, absolute=False, duration=0.2)
            mouse.drag(0, 0, -25, -50, absolute=False, duration=0.2)
            mouse.drag(0, 0, -50, -50, absolute=False, duration=0.2)
            