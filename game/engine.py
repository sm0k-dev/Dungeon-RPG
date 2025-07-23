import os, msvcrt
from game.menu import menu_bienvenida, menu_iniciar_juego
from game.entities.character import create_heroe
from game.world.locations import campamento_goblin, create_dungeon
from game.combat.battle import explore_location
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
            heroe = create_heroe(heroe_name)
            dungeon = create_dungeon(campamento_goblin)
            
            os.system('cls')
            print(f"\n¡Bienvenido {heroe['nombre']}! Tu aventura comienza en el {dungeon['name']}.\n")
            explore_result = explore_location(heroe, dungeon)
            print(explore_result)
            
        elif option == '2':
            print("¡Nos veremos en otro mundo Aventurero 💀!")
        else:
            print("Opción no válida. Intenta de nuevo.")
        #Player_Options

        msvcrt.getch()
