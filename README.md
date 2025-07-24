# Dungeon RPG

**Dungeon RPG** es un juego de rol (RPG, Role-Playing Game) por consola desarrollado en Python, basado en el género de combate por turnos. Inspirado en los generos clásicos como Final Fantasy y Chrono Trigger, el jugador explora mazmorras, enfrenta enemigos y progresa en la aventura tomando decisiones estratégicas en cada turno de combate.

## Características planeadas por ahora:

- Sistema de combate por turno.
- Múltiples enemigos y escenarios.
- Inventario y objetos.

## Estructura del Proyecto:

```
Dungeon RPG
├── main.py                     # Punto de entrada del juego                  
├── README.md                   # Explicación del juego y cómo ejecutarlo
│
├── game                        # Código fuente del juego
│   ├── engine.py               # Motor principal del juego (loop, lógica general)
│   ├── menu.py                 # Menús, inicio, opciones
│   ├── input_handler.py        # Entrada del usuario (lectura de comandos, validaciones)
│   │
│   ├── entities                # Entidades del juego: personaje, monstruos, NPCs
│   │   ├── character.py        # Lógica del jugador
│   │   └── monsters.py         # Lógica de monstruos
│   │
│   ├── combat                  # Sistema de combate
│   │   └── battle.py           # Control del combate
│   │
│   ├── world                   # Escenarios, mapa, exploración
│   │   └── locations.py        # Escenarios, calabozos, etc.
│   │
│   └── utils                   # Utilidades varias
│       └── helpers.py          # Funciones auxiliares
│
└── tests                       # (opcional) Pruebas unitarias
    └─ test_combat.py
```


## Cómo ejecutar el juego:

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando:

```bash
python main.py
```