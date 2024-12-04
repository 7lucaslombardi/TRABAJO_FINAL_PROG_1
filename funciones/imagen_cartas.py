import pygame
from datos.pantalla import *
from funciones.botones import *

# Tamaño de las cartas
TAMAÑO_CARTA = (110, 130)  # Ancho y Alto de las cartas
coordenadas_jugador = (230, 400) # Coordenadas iniciales de las cartas jugador
coordenadas_maquina = (230, 50) # Coordenadas iniciales de las cartas maquina
coordenadas_x_jugador = 230
coordenadas_y_jugador = 400
coordenadas_finales_jugador = (230, 250)
espacio_entre_cartas = 15

# Función para dibujar cartas en la pantalla
def dibujar_cartas(pantalla, cartas : list, coordenadas_x_jugador : int ,coordenadas_y_jugador : int ):
    '''
    Dibuja las cartas en la pantalla
    Recibe la pantalla, una lista de cartas y las coordenadas de x e y
    '''
    
    for carta in cartas:
        imagen_carta = carta["imagen"]  # Cada carta es un diccionario con una clave "imagen"
        pantalla.blit(imagen_carta, (coordenadas_x_jugador ,coordenadas_y_jugador))  # Dibujar la carta
        coordenadas_x_jugador += 120  # Separación horizontal
        


def mover_carta(pantalla, mano : list, coordenadas_iniciales : tuple, coordenadas_finales : tuple):
    '''
    Mueve las cartas de una posicion hacia otra
    Recibe la pantalla, una lista de cartas, coordenadas de inicio y de finalizacion
    '''
    
    (x,y) = coordenadas_iniciales
    (x_final,y_final) = coordenadas_finales
    velocidad = 5
    
    
    for carta in mano:
        imagen_carta = carta["imagen"]
        
        while y != y_final: # Bucle para mover la carta hasta que alcance la coordenada y_final
            
            if y < y_final:
                y += velocidad
            elif y > y_final:
                y -= velocidad

        
        coordenadas_finales = (x_final,y) # Se actualizan las coordenadas finales
        pantalla.blit(imagen_carta, (coordenadas_finales))  # Dibuja la carta
        pygame.display.flip()
        x_final += 120  # Separación horizontal entre cartas

def redibujar_pantalla(pantalla, cartas_jugador : list, lista_carta_jugador : list, lista_carta_maquina : list
                    , puntos_jugador : int, puntos_maquina : int):
    """
    Redibuja todos los elementos en la pantalla
    Recibe la pantalla, una lista de cartas del jugador, una lista de cartas vacia y una lista de cartas de la maquina
    """
    x, y = 170, 0       # Coordenadas del area
    ancho, alto = 500, ALTO  # Tamaño del área en píxeles
    area_cartas = pygame.Rect(x, y, ancho, alto) # Se actualiza determinada area de la pantalla

    pantalla.blit(fondo,area_cartas,area_cartas )  # Dibuja el fondo en la pantalla
    # Dibujar las cartas del jugador
    dibujar_cartas(pantalla, cartas_jugador, coordenadas_x_jugador, coordenadas_y_jugador)

    # Dibuja las cartas seleccionadas del jugador en la mesa
    mover_carta(pantalla, lista_carta_jugador, coordenadas_jugador, coordenadas_finales_jugador)
    # Dibuja las cartas seleccionadas de la maquina en la mesa
    mover_carta(pantalla, lista_carta_maquina, coordenadas_maquina, coordenadas_maquina)

    crear_boton(pantalla, f"Jugador: {puntos_jugador}", (50, 30), (100, 30), BLANCO, NEGRO, "comicsansms", 18) # Marcador del jugador
    crear_boton(pantalla, f"Maquina: {puntos_maquina}", (50, 80), (100, 30), BLANCO, NEGRO, "comicsansms", 18) # Marcador de la maquina
    pantalla.blit(imagen_mazo, (30, 430))  # Dibuja el mazo
    crear_boton(pantalla, "TRUCO", (700, 250), (80, 30), BLANCO, NEGRO, "comicsansms", 18)

    crear_boton(pantalla, "ENVIDO", (700, 300), (80, 30), BLANCO, NEGRO, "comicsansms", 18)
    pygame.display.update()

