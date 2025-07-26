import os, msvcrt
from game.screen_text import welcome_menu_text, get_hero_status_text, hero_options_text
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
            hero = create_hero()
            #Loop: Game_Menu
            while True:
                #Screen: Game_Menu
                os.system('cls')
                #Hero_Status
                print(get_hero_status_text(hero))
                #Hero_Options
                print(hero_options_text)
                option = input("Selecciona una opción: ")
                os.system('cls')
                #Screen

                #Menu_Options
                if option == '1': #Explore_Dungeons
                    print(get_hero_status_text(hero))
                    print("\nSelecciona un dungeon para explorar:\n")
                    for i in range(len(dungeons)):
                        print(f"{i + 1}. {dungeons[i]['name']}")
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