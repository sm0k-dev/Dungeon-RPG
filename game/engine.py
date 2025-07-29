import os, msvcrt
from game.screen_text import welcome_menu_text, get_hero_status_text, hero_options_text, get_dungeon_availables
from game.entities.character import create_hero
from game.world.dungeons import create_dungeon, dungeons
from game.combat.battle import explore_dungeon


def start_game():
    """Inicia el juego mostrando el menú principal y gestionando las opciones del usuario."""
    #Main_Menu
    #Loop: Main_Menu
    while True:
        #Screen: Main_Menu
        os.system('cls')
        print(welcome_menu_text)
        option = input("Selecciona una opción: ")
        os.system('cls')
        #Screen

        #Menu_Options
        if option == '1': #Play
            #Heroe_Creation
            heroe = create_hero()
            #Loop: Game_Menu
            while True:
                #Screen: Game_Menu
                os.system('cls')
                #Hero_Status
                print(get_hero_status_text(heroe))
                #Hero_Options
                print(hero_options_text)
                option = input("Selecciona una opción: ")
                # os.system('cls')

                #Menu de opciones del héroe
                if option == '1': #Explorar Dungeons
                    
                    #Selección del Dungeon
                    while True:
                        os.system('cls')
                        print(get_hero_status_text(heroe))
                        print(get_dungeon_availables(dungeons))
                        dungeon_choice = input("\nSelecciona un dungeon a explorar: ")
                        if not (dungeon_choice.isdigit() and 1 <= int(dungeon_choice) <= len(dungeons) + 1):
                            print(f"\nAventurero, ingresa una opción válida entre 1 y {len(dungeons)+1}.")
                            msvcrt.getch()
                            continue
                        dungeon_choice = int(dungeon_choice)
                        break
                    
                    # Creación y exploración del Dungeon
                    if dungeon_choice != len(dungeons) + 1:
                        dungeon = create_dungeon(dungeons[dungeon_choice - 1])
                        print(f"\n{heroe['nombre']} ha entrado en el dungeon: {dungeon['name']}")
                        explore_dungeon(heroe, dungeon)
                    
                    if heroe["salud"] == 0:
                        break
                    pass
                elif option == '2': #Shop
                    pass
                elif option == '3': #Rest
                    pass
                elif option == '4': #End_Adventure
                    print("¡Gracias por jugar! Hasta la próxima aventura.")
                    break
                else: #Invalid_Option
                    print("Opción no válida. Intenta de nuevo.")
                msvcrt.getch() #Wait_for_User_Input
                #Menu_Options
        elif option == '2': #Exit
            print("¡Nos veremos en otro mundo Aventurero 💀!")
            break
        else: #Invalid_Option
            print("Opción no válida. Intenta de nuevo.")
        #Menu_Options
        msvcrt.getch() #Wait_for_User_Input