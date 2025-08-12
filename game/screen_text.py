import os


# Texto del menu principal
welcome_menu_text = """
=== RPG-Fight ===
¡Bienvenido! Prepárate para la aventura.
          
1. Iniciar Juego
2. Salir del Juego

"""


# Texto de creación del héroe
hero_creation_text = """
=== Creación de Héroe ===
Iniciando tu aventura...

¿Cómo te llamas héroe?: """


# Texto de estado del héro
def get_hero_status_text(heroe: dict) -> str:
    return f"""
=== Estado de {heroe["name"]} ===
Salud: {heroe["health"]}
Nivel: {heroe["level"]}
Experiencia: {heroe["experience"]}
Daño: {heroe["attack"]}
Oro: {heroe["gold"]}
"""

# Texto del menu de opciones del héroe
hero_options_text = """
=== Opciones ===
1. Explorar Dungeons.
2. Tienda.
3. Posada.
4. Terminar el viaje.
"""


# Texto de selección de dungeons disponibles
def get_dungeon_availables_text(dungeons: list) -> str:
    dungeon_list_text = "\n=== Dungeons Disponibles ===\n"
    for i, dungeon in enumerate(dungeons):
        dungeon_list_text += f"{i + 1}. {dungeon['name']}\n"
    dungeon_list_text += f"{len(dungeons) + 1}. Volver"
    return dungeon_list_text


#Combat_Screen
def get_combat_menu_text(dungeon_name, heroe, monster, description="") -> str:
    """Actualiza y entrega a la terminal la información del combate según el turno correspondiente."""
    os.system('cls')
    return f"""===========================================================
  Dungeon: {dungeon_name}




                   Fotograma ASCII AQUI




-----------------------------------------------------------
  Heroe    : {heroe['name']}            | Lv.{heroe['level']} | HP: {heroe['health']}/{heroe['health_max']}
  Monstruo : {monster['name']}        | Lv.{heroe['level']} | HP: {monster['health']}/{monster['health_max']}

  Mensaje  : {description}

===========================================================
   [1] Atacar   [2] Bloquear   [3] Inventario   [4] Huir
==========================================================="""
