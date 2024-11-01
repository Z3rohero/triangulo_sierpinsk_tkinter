import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para dibujar un triángulo con turtle
def dibujarTriangulo(puntos, color, miTortuga):
    miTortuga.fillcolor(color)
    miTortuga.up()
    miTortuga.goto(puntos[0][0], puntos[0][1])
    miTortuga.down()
    miTortuga.begin_fill()
    miTortuga.goto(puntos[1][0], puntos[1][1])
    miTortuga.goto(puntos[2][0], puntos[2][1])
    miTortuga.goto(puntos[0][0], puntos[0][1])
    miTortuga.end_fill()

# Función para obtener el punto medio entre dos puntos
def obtenerMitad(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Función para dibujar el triángulo de Sierpinski recursivamente
def sierpinski(puntos, grado, miTortuga):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    dibujarTriangulo(puntos, colormap[grado], miTortuga)
    if grado > 0:
        sierpinski([puntos[0],
                    obtenerMitad(puntos[0], puntos[1]),
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)
        sierpinski([puntos[1],
                    obtenerMitad(puntos[0], puntos[1]),
                    obtenerMitad(puntos[1], puntos[2])],
                   grado - 1, miTortuga)
        sierpinski([puntos[2],
                    obtenerMitad(puntos[2], puntos[1]),
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)

# Función para iniciar la interfaz de usuario y recibir la profundidad
def iniciarInterfaz():
    # Crear la ventana de entrada con tkinter
    root = tk.Tk()
    root.title("Dibujo del Triángulo de Sierpinski")
    root.geometry("600x200")  
    root.config(bg="lightgray")  

    # Instrucciones
    instrucciones = tk.Label(root, text="Ingresa la profundidad del triángulo:", bg="lightgray",fg="black", font=("Arial", 12))
    instrucciones.pack(pady=10)

    # Variable para almacenar la profundidad
    grado = tk.IntVar()

    # Rango de profundidad
    rango_label = tk.Label(root, text="(0 a 3)",bg="lightgray",  fg="black", font=("Arial", 10))
    rango_label.pack()

    # Entrada para la profundidad
    entrada_grado = tk.Entry(root, textvariable=grado, font=("Arial", 14))
    entrada_grado.pack(pady=10)

    # Botón para dibujar
    def dibujar():
        if grado.get() is not None and 0 <= grado.get() <= 3:
            miTortuga = turtle.Turtle()
            miVentana = turtle.Screen()
            miVentana.title("Triángulo de Sierpinski")
            miTortuga.speed(0)  # Velocidad máxima
            misPuntos = [[-200, -100], [0, 200], [200, -100]]
            sierpinski(misPuntos, grado.get(), miTortuga)
            miVentana.exitonclick()
            root.destroy()  # Cerrar la ventana de entrada
        else:
            messagebox.showerror("Error", "Por favor ingresa un número válido entre 0 y 3.")

    # Botón de aceptar
    aceptar_btn = tk.Button(root, text="Dibujar", command=dibujar,  fg="black", bg="lightgreen", font=("Arial", 12))
    aceptar_btn.pack(pady=5)

    # Botón de cancelar
    cancelar_btn = tk.Button(root, text="Cancelar", command=root.quit,  fg="black", bg="salmon", font=("Arial", 12))
    cancelar_btn.pack(pady=5)

    # Iniciar la interfaz
    root.mainloop()

# Ejecutar la interfaz
iniciarInterfaz()

