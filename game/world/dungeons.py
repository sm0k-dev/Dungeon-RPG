from random import randint
from game.entities.monsters import create_monster

# Función para poblar un dungeon de forma aleatoria de su lista de monstruos
def create_dungeon(dungeon) -> dict:
    for i in range(len(dungeon["rooms"])):
        monster_type = dungeon["monsters"][randint(0, 1)]
        dungeon["rooms"][i] = create_monster(
            name=monster_type["name"],
            health=monster_type["health"],
            attack=monster_type["attack"],
            gold=monster_type["gold"],
            level=monster_type["level"],
        )
    return dungeon

# Diccionarios que representan un dungeon
goblin_camp = {
    "name": "Campamento Goblin",
    "rooms": [None] * 20,
    "monsters": [
        {"name": "Goblin", "health": 20, "attack": 5, "gold": 0, "level": 1},
        {"name": "Goblin Elite", "health": 30, "attack": 7, "gold": 5, "level": 3}
    ]
}

wolf_den = {
    "name": "Guarida de Lobos",
    "rooms": [None] * 20,
    "monsters": [
        {"name": "Lobo", "health": 18, "attack": 6, "gold": 0, "level": 2},
        {"name": "Lobo Alfa", "health": 32, "attack": 10, "gold": 7, "level": 5}
    ]
}

fallen_mausoleum = {
    "name": "Mausoleo de los Caídos",
    "rooms": [None] * 20,
    "monsters": [
        {"name": "Esqueleto", "health": 15, "attack": 4, "gold": 2, "level": 4},
        {"name": "Zombi", "health": 20, "attack": 8, "gold": 3, "level": 4}
    ]
}

orc_stronghold = {
    "name": "Bastión de Orcos",
    "rooms": [None] * 20,
    "monsters": [
        {"name": "Orco", "health": 25, "attack": 8, "gold": 4, "level": 5},
        {"name": "Orco Elite", "health": 35, "attack": 14, "gold": 10, "level": 10}
    ]
}


# Lista de todos los dungeons disponibles para explorar
dungeons = [goblin_camp, wolf_den, fallen_mausoleum, orc_stronghold]


