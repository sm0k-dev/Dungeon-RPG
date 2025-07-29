#Heroe_Statistics
def generate_hero_base_stats(nombre="Heroe") -> dict:
    """Genera un diccionario con las estadísticas base del héroe."""
    return {
        "nombre": nombre,
        "salud": 100,
        "mana": 100,
        "ataque": 10,
        "dinero": 0,
        "level": 1,
        "experiencia": 0
    }

#Heroe_Creation
def create_hero() -> dict:
    """Crea un héroe inicial con estadísticas base."""
    #Loads necessary text for character creation
    from game.screen_text import hero_creation_text

    #Prompts user for hero name
    hero_name = input(hero_creation_text)

    #Generates hero with base stats
    heroe = generate_hero_base_stats(hero_name)
    return heroe