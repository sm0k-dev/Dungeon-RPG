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
def get_hero_status_text(heroe) -> str:
    return f"""
=== Estado de {heroe["nombre"]} ===
Salud: {heroe["salud"]}
Nivel: {heroe["level"]}
Experiencia: {heroe["experiencia"]}
Daño: {heroe["ataque"]}
Oro: {heroe["dinero"]}
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

#Combat_Screen
def get_combat_menu_text(heroe, monster, description, heroe_damage, monster_damage) -> str:
    """Actualiza y entrega a la terminal la información del combate según el turno correspondiente."""
    return f"""







    
    
FOTOGRAMA ASCII AQUI
    
Lvl. {monster["nivel"]} {monster["nombre"]}: {monster["salud"]} {heroe_damage}
{description}
===============================================
|1. Atacar     | {" "*(len(heroe["nombre"])+2)}HP {" "*(len(str(heroe["salud"]))-2)}MP
|2. Magia      | {heroe["nombre"]}: {heroe["salud"]} {heroe["mana"]}
|3. Bloquear   | {" "*(len(heroe["nombre"])+2)}{monster_damage}
|4. Inventario |
|5. Huir       |
==============================================="""