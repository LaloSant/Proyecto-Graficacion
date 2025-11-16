# Menu del Proyecto - Guía de Uso

## Descripción

Se ha creado una pantalla de menú interactiva para tu proyecto de graficación con las siguientes características:

### Pantalla Principal del Menú

Cuando inicies la aplicación, verás el menú principal con 4 botones:

1. **Jugar** - Inicia el juego/aplicación
2. **Seleccionar Personaje** - Abre la pantalla de selección de personajes
3. **Niveles** - Abre la pantalla de niveles (a implementar)
4. **Salir** - Cierra la aplicación

### Pantalla de Selección de Personaje

Al hacer clic en "Seleccionar Personaje", verás 3 opciones:

1. **Kevin** - Personaje principal
2. **Don Corru** - Personaje secundario
3. **Cubo** - Placeholder (usando un dodecaedro)

Cada botón muestra una etiqueta con el nombre del personaje. Al seleccionar un personaje, se guarda la selección y se cierra el menú.

### Características

- **Botones Interactivos**: Los botones cambian de color cuando pasas el mouse sobre ellos
- **Navegación Intuitiva**: Un botón "Volver" para regresar al menú principal
- **Fondo Semi-transparente**: El menú tiene un fondo oscuro que ayuda a verlo mejor
- **Estado del Juego**: El menú gestiona diferentes estados del juego

### Estructura de Código

El menú está implementado en dos clases:

#### Clase `Button`
Representa un botón individual con:
- Posición (x, y)
- Tamaño (width, height)
- Etiqueta de texto
- Callback (función a ejecutar al hacer clic)
- Estados de color (normal y hover)

#### Clase `Menu`
Gestiona toda la interfaz del menú con:
- Estados: "main" (menú principal) y "personaje" (selección de personaje)
- Manejo de clicks del mouse
- Seguimiento del estado hover del mouse
- Rendering de botones y texto

### Integración con el Proyecto

El menú está integrado en `main.py`:
- Se crea una instancia de `Menu` en el constructor de `MainWindow`
- Se pasa al `InputHandler` para manejar entrada del usuario
- Se dibuja cuando `game_state == "menu"`
- Los callbacks actualizan el estado del juego

### Cómo Funciona

1. La aplicación inicia con `game_state = "menu"`
2. El menú se dibuja en cada frame mientras esté activo
3. El `InputHandler` detecta clicks del mouse y los convierte a coordenadas OpenGL
4. El menú verifica qué botón fue clickeado
5. Al hacer clic en un botón, se ejecuta su callback y el menú se desactiva

### Personalizaciones Disponibles

Puedes personalizar:
- Posiciones de los botones
- Tamaños de los botones
- Colores (modificar `color_normal`, `color_hover`, `color_text`)
- Etiquetas de los botones
- Callbacks para cada acción

### Próximos Pasos

Para extender el menú:
1. Agregar más estados (ej: "pausa", "configuración")
2. Implementar la pantalla de niveles
3. Agregar animaciones o transiciones
4. Agregar sonidos al hacer clic
