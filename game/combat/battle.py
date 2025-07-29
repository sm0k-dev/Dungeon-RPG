from random import randint

def combat(heroe, monster) -> str:
    """Ejecuta el combate por turnos entre el héroe y el monstruo. Devuelve a la terminal información respecto a la pelea."""
    import os, msvcrt
    from game.screen_text import get_combat_menu_text
    heroe_damage = ""
    monster_damage = ""
    #Loop: Combat
    while True:
        os.system('cls')
        block = False
        description = ""
        print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
        option = input("Selecciona una opción: ")
        if option == '1':   #Attack
            chance = randint(1,10) <= 9
            if chance:
                description = f"{heroe["nombre"]} ataca exitosamente al Goblin."
                heroe_damage = f"-{heroe["ataque"]}"
                os.system('cls')
                print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
                monster["salud"] -= heroe["ataque"]
            else:
                description = f"{heroe["nombre"]} falla el ataque."
                heroe_damage = "MISS"
                print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))   
        elif option == '2': #Magic
            pass
        elif option == '3': #Block
            description = f"{heroe["nombre"]} bloqueará el siguiente ataque"
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
            block = True
        elif option == '4': #Inventory
            pass
        elif option == '5': #Flee
            description = f"{heroe["nombre"]} intentó huir!"
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
        else:               #InvalidOption
            description = "Opción Invalida, intenta de nuevo"
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
        msvcrt.getch()
        
        heroe_damage = ""

        if monster["salud"] <= 0:
            monster["salud"] = 0
            description = f"{heroe["nombre"]} ha derrotado a {monster["nombre"]}." 
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
            break
        
        chance = randint(1,10) <= 9
        if chance:
            if block:
                description = f"{heroe["nombre"]} logró bloquear el ataque"
                monster_damage = f"-{int(monster["ataque"]*(50/100))}"
            else:
                description = f"{monster["nombre"]} atacó a {heroe["nombre"]}."
                monster_damage = f"-{monster["ataque"]}"
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
            if block:
                heroe["salud"] -= int(monster["ataque"]*(50/100))
            else:
                heroe["salud"] -= monster["ataque"]

        else:
            description = f"{monster["nombre"]} fallo al atacar a {heroe["nombre"]}."
            monster_damage = "MISS"
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
        msvcrt.getch()

        monster_damage = ""

        if heroe["salud"] <= 0:
            heroe["salud"] = 0
            description = f"{heroe["nombre"]} ha sido derrotado." 
            os.system('cls')
            print(get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage))
            break
    msvcrt.getch()
    
    
def explore_dungeon(heroe, dungeon) -> str:
    # #Exploration
    for monster in dungeon["rooms"]:
        if monster is not None:
            while True:
                decision = input(f"\n¿Te has topado con un {monster['nombre']}, deseas pelear? (s/n): ").strip().lower()
                if decision == 's':
                    combat(heroe, monster)
                    break
                elif decision == 'n':
                    return f"\n{heroe['nombre']} decide retirarse de {dungeon['name']}."
                else:
                    print("Por favor, responde con 's' para sí o 'n' para no.")
            if heroe["salud"] <= 0:
                break
    #Exploration
    
    #Exploration Result
    if heroe["salud"] > 0:
        return f"{heroe['nombre']} ha explorado completamente {dungeon['name']}."
    else:
        return f"{heroe['nombre']} no puede continuar explorando debido a sus heridas."
     #Exploration Result