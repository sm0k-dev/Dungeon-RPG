import os, msvcrt
from game.screen_text import welcome_menu_text, get_hero_status_text, hero_options_text, get_dungeon_availables_text
from game.entities.character import generate_hero
from game.world.dungeons import create_dungeon, dungeons
from game.combat.battle import explore_dungeon


def start_game():
    """Inicia el juego mostrando el menú principal y gestionando las opciones del usuario."""
    #Menu Principal
    while True:
        # Muestra el menú principal
        os.system('cls')
        print(welcome_menu_text)
        option = input("Selecciona una opción: ")
        os.system('cls')

        # Opciones del menú principal
        if option == '1': #Iniciar Juego
            # Genera un héroe con un nombre ingresado por el usuario
            heroe = generate_hero()
            
            #Loop: Estado y opciones de menu del héroe
            while True:
                os.system('cls')
                # Estado del héroe
                print(get_hero_status_text(heroe))
                # Opciones de menu del héroe
                print(hero_options_text)
                option = input("Selecciona una opción: ")

                # Menu de opciones del héroe
                if option == '1': #Explorar Dungeons
                    
                    #Selección del Dungeon
                    while True:
                        os.system('cls')
                        # Estado del héroe
                        print(get_hero_status_text(heroe))
                        # Lista de dungeons disponibles
                        print(get_dungeon_availables_text(dungeons))
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
                        print(f"\n{heroe['name']} ha entrado en el dungeon: {dungeon['name']}")
                        result_dungeon = explore_dungeon(heroe, dungeon)
                        print(result_dungeon)
                        print("Presiona cualquier tecla para continuar...")
                        msvcrt.getch()               
                elif option == '2': #Tienda
                    # Aquí se implementaría la lógica de la tienda
                    print("La tienda aún no está implementada 😥.")
                    msvcrt.getch()
                    pass
                elif option == '3': #Posada
                    # Aquí se implementaría la lógica de la posada
                    print("La posada aún no está implementada 😥.")
                    msvcrt.getch()
                    pass
                elif option == '4': #Terminar el viaje
                    print(f"¡Gracias por jugar!. Hasta la próxima aventura {heroe['name']}.")
                    break
                else: #Opción no válida
                    print("Opción no válida. Intenta de nuevo.")
                    msvcrt.getch()
                # Fin opciones del menú del héroe
                
        elif option == '2': #Salir del Juego
            print("¡Nos veremos en otro mundo Aventurero 💀!")
            break
        else: #Opción no válida
            print("Opción no válida. Intenta de nuevo.")
        # Fin opciones del menú principal
        msvcrt.getch()