import pygame
import sys

# Función para dibujar un triángulo
def dibujar_triangulo(screen, puntos, color):
    pygame.draw.polygon(screen, color, puntos)

# Función para obtener el punto medio entre dos puntos
def obtener_mitad(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

# Función para dibujar el triángulo de Sierpinski recursivamente
def sierpinski(screen, puntos, grado):
    colormap = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]  # Colores en RGB
    dibujar_triangulo(screen, puntos, colormap[grado])
    
    if grado > 0:
        sierpinski(screen, [puntos[0],
                            obtener_mitad(puntos[0], puntos[1]),
                            obtener_mitad(puntos[0], puntos[2])],
                   grado - 1)
        sierpinski(screen, [puntos[1],
                            obtener_mitad(puntos[0], puntos[1]),
                            obtener_mitad(puntos[1], puntos[2])],
                   grado - 1)
        sierpinski(screen, [puntos[2],
                            obtener_mitad(puntos[2], puntos[1]),
                            obtener_mitad(puntos[0], puntos[2])],
                   grado - 1)

# Función principal
def main():
    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Triángulo de Sierpinski")

    # Solicitar la profundidad al usuario
    while True:
        grado = input("Ingresa el número de profundidad del triángulo (0 a 3): ")
        if grado.isdigit() and 0 <= int(grado) <= 3:
            grado = int(grado)
            break
        else:
            print("Por favor ingresa un número válido entre 0 y 3.")

    # Puntos del triángulo
    misPuntos = [[200, 50], [100, 350], [300, 350]]
    
    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Limpiar la pantalla
        screen.fill((255, 255, 255))
        
        # Dibujar el triángulo de Sierpinski
        sierpinski(screen, misPuntos, grado)
        
        # Actualizar la pantalla
        pygame.display.flip()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
