import turtle

# Definir el tamaño del laberinto
ANCHO_CELDA = 20
FILAS = 11
COLUMNAS = 21

# Crear una ventana de Turtle
ventana = turtle.Screen()
ventana.setup(1200, 600, True)
ventana.bgcolor("white")

# Crear el objeto Turtle
laberinto_turtle = turtle.Turtle()
laberinto_turtle.speed(0)  # Configurar la velocidad del dibujo

# Posición inicial de la tortuga
INICIO_X = 0
INICIO_Y = (FILAS - 1) * ANCHO_CELDA
laberinto_turtle.penup()
laberinto_turtle.goto(INICIO_X, INICIO_Y)
laberinto_turtle.pendown()

# Dirección inicial de la tortuga
DIRECCION_ACTUAL = "up"

# Laberinto de ejemplo (1: pared, 0: pasillo)
LABERINTO = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
]

# Dibujar una celda
def dibujar_celda(x, y):
    laberinto_turtle.color("black", "black")
    laberinto_turtle.begin_fill()
    laberinto_turtle.penup()
    laberinto_turtle.goto(x, y)
    laberinto_turtle.pendown()
    for _ in range(4):
        laberinto_turtle.forward(ANCHO_CELDA)
        laberinto_turtle.right(90)
    laberinto_turtle.end_fill()

# Dibujar el laberinto
def dibujar_laberinto():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if LABERINTO[fila][columna] == 1:
                dibujar_celda(columna * ANCHO_CELDA, (fila * ANCHO_CELDA) * -1)

# Inicializar el laberinto
dibujar_laberinto()

# Posicionar la tortuga para empezar
laberinto_turtle.penup()
laberinto_turtle.goto(30, 0)
laberinto_turtle.pendown()

# Configurar la tortuga como cursor
laberinto_turtle.shape("turtle")
laberinto_turtle.color("red")

# Mover la tortuga hacia adelante
def mover_adelante():
    global DIRECCION_ACTUAL
    siguiente_x, siguiente_y = laberinto_turtle.xcor(), laberinto_turtle.ycor()

    if DIRECCION_ACTUAL == "up":
        siguiente_y += (ANCHO_CELDA / 2)
    elif DIRECCION_ACTUAL == "down":
        siguiente_y -= (ANCHO_CELDA / 2)
    elif DIRECCION_ACTUAL == "left":
        siguiente_x -= (ANCHO_CELDA / 2)
    elif DIRECCION_ACTUAL == "right":
        siguiente_x += (ANCHO_CELDA / 2)

    # Verificar si la próxima posición está dentro de un pasillo
    fila = int(-siguiente_y / ANCHO_CELDA)
    columna = int(siguiente_x / ANCHO_CELDA)

    if 0 <= fila < FILAS and 0 <= columna < COLUMNAS and LABERINTO[fila][columna] == 0:
        laberinto_turtle.goto(siguiente_x, siguiente_y)

# Girar la tortuga a la izquierda
def girar_izquierda():
    global DIRECCION_ACTUAL
    if DIRECCION_ACTUAL == "up":
        DIRECCION_ACTUAL = "left"
        laberinto_turtle.setheading(180)
    elif DIRECCION_ACTUAL == "down":
        DIRECCION_ACTUAL = "right"
        laberinto_turtle.setheading(0)
    elif DIRECCION_ACTUAL == "left":
        DIRECCION_ACTUAL = "down"
        laberinto_turtle.setheading(270)
    elif DIRECCION_ACTUAL == "right":
        DIRECCION_ACTUAL = "up"
        laberinto_turtle.setheading(90)

# Girar la tortuga a la derecha
def girar_derecha():
    global DIRECCION_ACTUAL
    if DIRECCION_ACTUAL == "up":
        DIRECCION_ACTUAL = "right"
        laberinto_turtle.setheading(0)
    elif DIRECCION_ACTUAL == "down":
        DIRECCION_ACTUAL = "left"
        laberinto_turtle.setheading(180)
    elif DIRECCION_ACTUAL == "left":
        DIRECCION_ACTUAL = "up"
        laberinto_turtle.setheading(90)
    elif DIRECCION_ACTUAL == "right":
        DIRECCION_ACTUAL = "down"
        laberinto_turtle.setheading(270)

# Asociar eventos de teclado a funciones
ventana.onkey(mover_adelante, "w")
ventana.onkey(girar_izquierda, "a")
ventana.onkey(girar_derecha, "d")

# Escuchar eventos de teclado
ventana.listen()

# Mantener la ventana abierta
ventana.mainloop()
