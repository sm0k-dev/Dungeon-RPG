#Main_Menu
welcome_menu_text = """
=== RPG-Fight ===
¡Bienvenido! Prepárate para la aventura.
          
1. Iniciar Juego
2. Salir del Juego

"""
#Main_Menu
    
#Hero_Creation
hero_creation_text = """
=== Creación de Héroe ===
Iniciando tu aventura...

¿Cómo te llamas héroe?: """
#Hero_Creation

#Hero_Status
def get_hero_status_text(hero) -> str:
    """Recibe un diccionario con las estadísticas del héroe y devuelve un texto formateado."""
    return f"""
=== Estado de {hero["name"]} ===
Salud: {hero["health"]}
Nivel: {hero["level"]}
Experiencia: {hero["experience"]}
Daño: {hero["damage"]}
Oro: {hero["gold"]}
"""
#Hero_Status

#Hero_Options
hero_options_text = f"""
=== Opciones ===
1. Explorar Dungeons.
2. Comprar objetos.
3. Descansar.
4. Terminar viaje.
"""
#Hero_Options