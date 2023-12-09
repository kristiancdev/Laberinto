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

# Cerrar la ventana al hacer clic
ventana.exitonclick()
