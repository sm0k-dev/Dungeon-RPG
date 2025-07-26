from random import randint
from game.entities.monsters import create_monster

# Función para poblar un dungeon de forma aleatoria de su lista de monstruos
def create_dungeon(dungeon) -> dict:
    for i in range(len(dungeon["rooms"])):
        monster_type = dungeon["monsters"][randint(0, 1)]
        dungeon["rooms"][i] = create_monster(
            nombre=monster_type["nombre"],
            salud=monster_type["salud"],
            ataque=monster_type["ataque"]
        )
    return dungeon

# Diccionarios que representan un dungeon
goblin_camp = {
    "name": "Campamento Goblin",
    "rooms": [None] * 20,
    "monsters": [
        {"nombre": "Goblin", "salud": 20, "ataque": 5},
        {"nombre": "Goblin Elite", "salud": 30, "ataque": 7}
    ]
}

wolf_den = {
    "name": "Guarida de Lobos",
    "rooms": [None] * 20,
    "monsters": [
        {"nombre": "Lobo", "salud": 18, "ataque": 6},
        {"nombre": "Lobo Alfa", "salud": 32, "ataque": 10}
    ]
}

fallen_mausoleum = {
    "name": "Mausoleo de los Caídos",
    "rooms": [None] * 20,
    "monsters": [
        {"nombre": "Esqueleto", "salud": 15, "ataque": 4},
        {"nombre": "Zombi", "salud": 20, "ataque": 8}
    ]
}

orc_stronghold = {
    "name": "Bastión de Orcos",
    "rooms": [None] * 20,
    "monsters": [
        {"nombre": "Orco", "salud": 25, "ataque": 8},
        {"nombre": "Orco Elite", "salud": 35, "ataque": 14}
    ]
}


# Lista de todos los dungeons disponibles para explorar
dungeons = [goblin_camp, wolf_den, fallen_mausoleum, orc_stronghold]


