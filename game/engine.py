import os, msvcrt
from game.menu import *
from game.entities.character import heroe
from game.entities.monsters import monster
from game.combat.battle import combat
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
            monster_gen = monster("Orco", 50, 10)
            os.system('cls')
            combat_result = combat(heroe_character, monster_gen)
            print(combat_result)
        elif option == '2':
            print("¡Nos veremos en otro mundo Aventurero 💀!")
        else:
            print("Opción no válida. Intenta de nuevo.")
        #Player_Options

        msvcrt.getch()
