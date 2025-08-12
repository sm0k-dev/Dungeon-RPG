import os, msvcrt
from random import randint
from game.screen_text import get_combat_menu_text

def combat(dungeon_name, heroe, monster) -> str:
    """Ejecuta el combate por turnos entre el héroe y el monstruo. Devuelve a la terminal información respecto a la pelea."""
    #Loop: Combat
    while True:
        # Turno del héroe
        os.system('cls')
        block = False
        description = "Es tu turno, elige una acción."
        print(get_combat_menu_text(dungeon_name, heroe, monster, description))
        option = input("Selecciona una opción: ")
        if option == '1':   #Atacar
            chance = randint(1,10) <= 9
            if chance:
                description = f"⚔️  {heroe['name']} lanza un poderoso ataque contra {monster['name']} y le causa daño! 💥"
                monster["health"] -= heroe["attack"]
            else:
                description = f"😥  {heroe['name']} intenta atacar, pero {monster['name']} esquiva hábilmente el golpe!"
        elif option == '2': #Bloquear
            block = True
            description = f"🛡️  {heroe['name']} se prepara y levanta su escudo, ¡el próximo ataque será reducido a la mitad!"
        elif option == '3': #Inventario
            description = "🎒  El inventario aún está en construcción."
            print(get_combat_menu_text(dungeon_name, heroe, monster, description))
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch()
            continue
        elif option == '4': #Huir
            escape_chance = randint(1, 10) <= 7
            if escape_chance:
                description = f"🏃‍♂️  {heroe['name']} corre con todas sus fuerzas y logra escapar de las garras de {monster['name']}!"
                print(get_combat_menu_text(dungeon_name, heroe, monster, description))
                print("Presiona cualquier tecla para continuar...")
                msvcrt.getch()
                break
            else:
                description = f"🏃‍♂️  {heroe['name']} intentó huir, pero el monstruo {monster['name']} lo alcanzó!"
        else:               #Opción inválida
            description = "❌ Opción inválida."
            print(get_combat_menu_text(dungeon_name, heroe, monster, description))
            print("Presiona cualquier tecla para continuar...")
            msvcrt.getch() 
            continue 
        print(get_combat_menu_text(dungeon_name, heroe, monster, description))
        
        # Verifica si el monstruo ha sido derrotado
        if monster["health"] <= 0:
            monster["health"] = 0
            description = f"🎉 {heroe['name']} ha derrotado a {monster['name']} y la mazmorra tiembla ante su victoria."
            print(get_combat_menu_text(dungeon_name, heroe, monster, description))
            break
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
        
        # Turno del monstruo
        chance = randint(1,10) <= 9
        if chance:
            if block:
                description = f"🛡️  {heroe['name']} bloquea el ataque de {monster['name']} y solo recibe la mitad del daño."
                heroe["health"] -= int(monster["attack"]*(50/100))
            else:
                description = f"💢 {monster['name']} lanza un ataque feroz contra {heroe['name']} y le causa daño!"
                heroe["health"] -= monster["attack"]
        else:
            description = f"😅  {monster['name']} intenta atacar, pero falla y {heroe['name']} esquiva con agilidad!"
        print(get_combat_menu_text(dungeon_name, heroe, monster, description))

        if heroe["health"] <= 0:
            heroe["health"] = 0
            description = f"☠️  {heroe['name']} ha caído en batalla. ¡La leyenda termina aquí... por ahora!"
            print(get_combat_menu_text(dungeon_name, heroe, monster, description))
            break
        print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()
    
    
def explore_dungeon(heroe, dungeon) -> str:
    dungeon_name = dungeon["name"]
    # #Exploration
    for monster in dungeon["rooms"]:
        while True:
            decision = input(f"\n¿Te has topado con un {monster['name']}, deseas pelear? (s/n): ").strip().lower()
            if decision == 's':
                combat(dungeon_name, heroe, monster)
                break
            elif decision == 'n':
                return f"\n{heroe['name']} decide retirarse de {dungeon['name']}."
            else:
                print("Por favor, responde con 's' para sí o 'n' para no.")
        if heroe["health"] <= 0:
            break
    #Exploration
    
    #Exploration Result
    if heroe["health"] > 0:
        return f"{heroe['name']} ha explorado completamente {dungeon['name']}."
    else:
        return f"{heroe['name']} no puede continuar explorando debido a sus heridas."
     #Exploration Result