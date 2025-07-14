import os, msvcrt
from game.menu import *
from game.entities.character import heroe

def start_game():
    while True:
        #Screen
        os.system('cls')
        print(menu_bienvenida)
        option = input("Selecciona una opción: ")
        os.system('cls')
        #Screen

        #Player_Options
        if option == '1':
            heroe_name = input(menu_iniciar_juego)
            heroe_character = heroe(heroe_name)
            
            print(heroe_character)
            
            pass
        elif option == '2':
            print("¡Nos veremos en otro mundo Aventurero 💀!")
            pass
        else:              
            print("Opción no válida. Intenta de nuevo.")
        #Player_Options

        msvcrt.getch()
