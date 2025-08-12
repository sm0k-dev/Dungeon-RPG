from game.screen_text import hero_creation_text


# Creación del héroe
def create_hero(hero_name="Hero") -> dict:
    """Retorna un diccionario con estadísticas base del héroe."""
    return {
        "name": hero_name,
        "health_max": 100,
        "health": 100,
        "mana": 100,
        "attack": 10,
        "gold": 0,
        "level": 1,
        "experience": 0
    }
    

# Generación del héroe
def generate_hero() -> dict:
    """Genera un héroe con un nombre ingresado por el usuario."""
    hero_name = input(hero_creation_text)
    heroe = create_hero(hero_name)
    return heroe