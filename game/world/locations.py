from random import randint
from game.entities.monsters import create_monster


campamento_goblin = {
    "name": "Campamento Goblin",
    "rooms": [None] * 20,
    "monsters": [
        {"nombre": "Goblin", "salud": 20, "ataque": 5},
        {"nombre": "Goblin Elite", "salud": 30, "ataque": 7}
    ]
}

def create_dungeon(dungeon) -> dict:
    for i in range(len(dungeon["rooms"])):
        monster_type = dungeon["monsters"][randint(0, 1)]
        dungeon["rooms"][i] = create_monster(
            nombre=monster_type["nombre"],
            salud=monster_type["salud"],
            ataque=monster_type["ataque"]
        )
    return dungeon
