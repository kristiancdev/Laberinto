import turtle

# Definir el tamaño del laberinto
ancho_celda = 20
filas = 11
columnas = 21

# Crear una ventana de Turtle
ventana = turtle.Screen()
ventana.setup(1200, 600, True)
ventana.bgcolor("white")

# Crear el objeto Turtle
laberinto_turtle = turtle.Turtle()
laberinto_turtle.speed(0)  # Configurar la velocidad del dibujo

# Posición inicial de la tortuga
inicio_x = 0
inicio_y = (filas - 1) * ancho_celda
laberinto_turtle.penup()
laberinto_turtle.goto(inicio_x, inicio_y)
laberinto_turtle.pendown()

# Dirección inicial de la tortuga
direccion_actual = "up"

# Función para dibujar una celda
def dibujar_celda(x, y):
    laberinto_turtle.color("black", "black")
    laberinto_turtle.begin_fill()
    laberinto_turtle.penup()
    laberinto_turtle.goto(x, y)
    laberinto_turtle.pendown()
    laberinto_turtle.forward(ancho_celda)
    laberinto_turtle.right(90)
    laberinto_turtle.forward(ancho_celda)
    laberinto_turtle.right(90)
    laberinto_turtle.forward(ancho_celda)
    laberinto_turtle.right(90)
    laberinto_turtle.forward(ancho_celda)
    laberinto_turtle.right(90)
    laberinto_turtle.end_fill()

# Función para dibujar el laberinto
def dibujar_laberinto():
    for fila in range(filas):
        for columna in range(columnas):
            if laberinto[fila][columna] == 1:
                dibujar_celda(columna * ancho_celda, (fila * ancho_celda)*-1)

# Laberinto de ejemplo (1: pared, 0: pasillo)
laberinto = [
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

# Dibujar el laberinto
dibujar_laberinto()

laberinto_turtle.penup()
laberinto_turtle.goto(30, 0)
laberinto_turtle.pendown()



# Asociar eventos de teclado a funciones
def mover_adelante():
    global direccion_actual
    if direccion_actual == "up" and laberinto_turtle.ycor() < (filas - 1) * (ancho_celda/2):
        laberinto_turtle.setheading(90)
        laberinto_turtle.forward((ancho_celda/2))
    elif direccion_actual == "down" and laberinto_turtle.ycor() > 0:
        laberinto_turtle.setheading(270)
        laberinto_turtle.forward((ancho_celda/2))
    elif direccion_actual == "left" and laberinto_turtle.xcor() > 0:
        laberinto_turtle.setheading(180)
        laberinto_turtle.forward((ancho_celda/2))
    elif direccion_actual == "right" and laberinto_turtle.xcor() < (columnas - 1) * (ancho_celda/2):
        laberinto_turtle.setheading(0)
        laberinto_turtle.forward((ancho_celda/2))

def girar_izquierda():
    global direccion_actual
    if direccion_actual == "up":
        direccion_actual = "left"
        laberinto_turtle.setheading(180)
    elif direccion_actual == "down":
        direccion_actual = "right"
        laberinto_turtle.setheading(0)
    elif direccion_actual == "left":
        direccion_actual = "down"
        laberinto_turtle.setheading(270)
    elif direccion_actual == "right":
        direccion_actual = "up"
        laberinto_turtle.setheading(90)

def girar_derecha():
    global direccion_actual
    if direccion_actual == "up":
        direccion_actual = "right"
        laberinto_turtle.setheading(0)
    elif direccion_actual == "down":
        direccion_actual = "left"
        laberinto_turtle.setheading(180)
    elif direccion_actual == "left":
        direccion_actual = "up"
        laberinto_turtle.setheading(90)
    elif direccion_actual == "right":
        direccion_actual = "down"
        laberinto_turtle.setheading(270)

# Asociar eventos de teclado a funciones
ventana.onkey(mover_adelante, "w")
ventana.onkey(girar_izquierda, "a")
ventana.onkey(girar_derecha, "d")

# Escuchar eventos de teclado
ventana.listen()

# Mantener la ventana abierta
ventana.mainloop()
