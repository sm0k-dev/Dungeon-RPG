#Heroe_Statistics
def generate_hero_base_stats(nombre="Heroe") -> dict:
    """Genera un diccionario con las estadísticas base del héroe."""
    return {
        "name": nombre,  #Heroe: Name
        "health": 100,   #Heroe: Health_Points
        "damage": 10,    #Heroe: Damage_Points
        "gold": 0,       #Heroe: Gold
        "level": 1,      #Heroe: Level
        "experience": 0, #Heroe: Experience_Points
    }

#Heroe_Creation
def create_hero() -> dict:
    """Crea un héroe inicial con estadísticas base."""
    #Loads necessary text for character creation
    from game.screen_text import hero_creation_text

    #Prompts user for hero name
    hero_name = input(hero_creation_text)

    #Generates hero with base stats
    hero = generate_hero_base_stats(hero_name)
    return hero