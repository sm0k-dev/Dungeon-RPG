# 🗡 RPG-Fight

**RPG-Fight** es un juego de rol por consola desarrollado en Python. El jugador combate contra enemigos en un sistema de combate por turnos.


## 📁 Estructura del Proyecto

```
RPG-Fight
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


## ▶️ Cómo ejecutar el juego

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando:

```bash
python main.py
```


## 🧱 Dependencias

Este proyecto no requiere librerías externas. Está construido solamente con módulos estándar de Python.


## 🛠️ Características planeadas por ahora

- Sistema de combate por turno.
- Múltiples enemigos y escenarios.
- Inventario y objetos.

