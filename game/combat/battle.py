from random import randint

def combat(heroe, monster) -> str:
    #Combat_Loop
    turno = 1
    while heroe["salud"] > 0 and monster["salud"] > 0:
        #Heroe_Turn
        print(f"\nTurno {turno} | {heroe['nombre']} [HP: {heroe['salud']}] vs {monster['nombre']} [HP: {monster['salud']}]")
        chance = randint(1, 10) > 3
        if chance:
            print(f"{heroe['nombre']} ataca a {monster['nombre']}!")
            monster["salud"] -= heroe["ataque"]
            print(f"{monster['nombre']} tiene {monster['salud']} de salud restante.")
        else:
            print(f"{heroe['nombre']} falla el ataque.")
        #Heroe_Turn

        #Check if monster is defeated
        if monster["salud"] <= 0:
            break

        #Monster_Turn
        chance = randint(1, 10) > 5
        if chance:
            print(f"{monster['nombre']} ataca a {heroe['nombre']}!")
            heroe["salud"] -= monster["ataque"]
            print(f"{heroe['nombre']} tiene {heroe['salud']} de salud restante.")
        else:
            print(f"{monster['nombre']} falla el ataque.")
        turno += 1
        #Monster_Turn
    #Combat_Loop

    #Combat_Result
    if heroe["salud"] <= 0:
        return f"\nDerrota!\n{heroe['nombre']} ha sido derrotado por el {monster['nombre']}."
    else:
        return f"\nVictoria!\n{heroe['nombre']} ha derrotado al {monster['nombre']}."
    #Combat_Result
    
    
def explore_dungeon(heroe, dungeon) -> str:
    # #Exploration
    for monster in dungeon["rooms"]:
        if monster is not None:
            while True:
                decision = input(f"\n¿Te has topado con un {monster['nombre']}, deseas pelear? (s/n): ").strip().lower()
                if decision == 's':
                    combat_result = combat(heroe, monster)
                    print(combat_result)
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