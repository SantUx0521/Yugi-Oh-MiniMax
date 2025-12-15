# Yugi-Oh-MiniMax
---

## Tecnologías
- Python 3.x
- Estructura modular: controller / model / view
- Algoritmo Minimax (con posibilidad de poda/ajustes en la implementación)

## Funcionalidades principales
- Simulación básica de partidas por turnos.
- Módulo AI que utiliza Minimax para elegir movimientos.
- Separación clara entre lógica de juego (model), controladores (controller) y presentación (view).

## Estructura del proyecto (resumen)
- main.py — punto de entrada.
- controller/ — controladores del juego y la IA.
- model/ — modelos de cartas y estado de juego.
- view/ — presentación/interfaz del juego.

## Instalación y ejecución
1. Clonar o descomprimir el proyecto.
2. Ejecutar desde la raíz del proyecto:
    ```
    python main.py
    ```
3. Para ajustar la dificultad/altura de búsqueda de la IA, editar el parámetro correspondiente en `controller/ai_minimax.py`.

## Desarrollo y contribuciones
- Seguir la separación MVC al agregar nuevas reglas o cartas.
- Añadir pruebas unitarias para la lógica en `model/`.
- Abrir issues o pull requests describiendo cambios propuestos.

## Autores
- Juan Sebastian Aragón Campo 
- Johan Sebastian Laverde 
- Diego Gomez Puentes
- Santiago Useche
- Sofia Carolina Quenoran
