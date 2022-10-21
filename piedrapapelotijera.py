# veamos si sale el juego

import random
from secrets import choice

while True:
    choices=['piedra','papel','tijera']
    computer=random.choice (choices)
    player= None

    while player not in choices:
        player = input('piedra, papel o tijera ?:  ').lower()
    if player == computer:
        print ('Maquina: ', computer)
        print('Jugador: ', player)
        print('Empate!')

    elif player == 'piedra':
     if computer=='papel':
         print ('Maquina: ', computer)
         print('Jugador: ', player)
         print('Perdiste! ')
         if computer=='tijera':
            print('Maquina: ', computer)
            print('Jugador: ', player)
            print('Ganaste!')

    elif player == 'tijera':
        if computer == 'piedra':
            print('Maquina: ', computer)
            print('Jugador: ', player)
            print('Perdiste! ')
        if computer == 'papel':
            print('Maquina: ', computer)
            print('Jugador: ', player)
            print('Ganaste!')

    elif player == 'papel':
        if computer == 'tijera':
            print('Maquina: ', computer)
            print('Jugador:' , player)
            print('Perdiste! ')
        if computer == 'piedra':
            print('Maquina: ', computer)
            print('Jugador: ', player)
            print('Ganaste!')

    play_again = input('Jugamos de nuevo? (si/no): ').lower()

    if play_again != 'si':
        break

print('Hasta luego!')
