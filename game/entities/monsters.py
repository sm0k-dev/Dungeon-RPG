def create_monster(nombre="Goblin", salud=20, ataque=5, nivel=1) -> dict:
    return {
        "nombre": nombre,
        "salud": salud,
        "ataque": ataque,
        "nivel": nivel
    }