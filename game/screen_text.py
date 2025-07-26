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
    return f"""
=== Estado de {hero["nombre"]} ===
Salud: {hero["salud"]}
Nivel: {hero["level"]}
Experiencia: {hero["experiencia"]}
Daño: {hero["ataque"]}
Oro: {hero["dinero"]}
"""
#Hero_Status

#Hero_Options
hero_options_text = """
=== Opciones ===
1. Explorar Dungeons.
2. Comprar objetos.
3. Descansar.
4. Terminar viaje.
"""
#Hero_Options

#Dungeons_Availables
def get_dungeon_availables(dungeons) -> str:
    dungeon_list_text = "\n=== Dungeons Disponibles ===\n"
    for i, dungeon in enumerate(dungeons):
        dungeon_list_text += f"{i + 1}. {dungeon['name']}\n"
    dungeon_list_text += f"{len(dungeons) + 1}. Volver"
    return dungeon_list_text
#Dungeons_Availables