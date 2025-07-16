def combat(heroe_character, monster_gen) -> str:
    #Encounter
    print(f"{heroe_character['nombre']} se ha topado con un {monster_gen['nombre']}!")

    from random import randint
    #Combat_Loop
    turno = 1
    while heroe_character["salud"] > 0 and monster_gen["salud"] > 0:
        #Heroe_Turn
        print(f"\nTurno {turno} | {heroe_character['nombre']} [HP: {heroe_character['salud']}] vs {monster_gen['nombre']} [HP: {monster_gen['salud']}]")
        chance = randint(1, 10) > 3
        if chance:
            print(f"{heroe_character['nombre']} ataca a {monster_gen['nombre']}!")
            monster_gen["salud"] -= heroe_character["ataque"]
            print(f"{monster_gen['nombre']} tiene {monster_gen['salud']} de salud restante.")
        else:
            print(f"{heroe_character['nombre']} falla el ataque.")
        #Heroe_Turn

        #Check if monster is defeated
        if monster_gen["salud"] <= 0:
            break

        #Monster_Turn
        chance = randint(1, 10) > 5
        if chance:
            print(f"{monster_gen['nombre']} ataca a {heroe_character['nombre']}!")
            heroe_character["salud"] -= monster_gen["ataque"]
            print(f"{heroe_character['nombre']} tiene {heroe_character['salud']} de salud restante.")
        else:
            print(f"{monster_gen['nombre']} falla el ataque.")
        turno += 1
        #Monster_Turn
    #Combat_Loop

    #Combat_Result
    if heroe_character["salud"] <= 0:
        return f"\nDerrota!\n{heroe_character['nombre']} ha sido derrotado por el {monster_gen['nombre']}."
    else:
        return f"\nVictoria!\n{heroe_character['nombre']} ha derrotado al {monster_gen['nombre']}."
    #Combat_Result