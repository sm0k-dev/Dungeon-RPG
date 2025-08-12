def create_monster(name="Goblin", health=20, attack=5, gold=0, level=1) -> dict:
    """Retorna un diccionario con estadísticas base del mounstro."""
    return {
        "name": name,
        "health_max": health,
        "health": health,
        "attack": attack,
        "gold": gold,
        "level": level,
        "experience": 0
    }