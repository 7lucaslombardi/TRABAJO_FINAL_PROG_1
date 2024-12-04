import pygame
from datos.colores import NEGRO, BLANCO


def crear_boton(pantalla, texto : str, posicion : tuple, tamaño : tuple, color_boton, color_texto, nombre_fuente : str, tamaño_fuente : int):
    """
    Dibuja un boton con un texto centrado.
    Recibe la pantalla, el texto a mostrar, la posicion del boton y el tamaño del boton 
    """
    fuente = pygame.font.SysFont(nombre_fuente, tamaño_fuente)  # Fuente predeterminada
    x, y = posicion
    ancho, alto = tamaño
    rectangulo = pygame.Rect(x, y, ancho, alto)

    # Dibujar el botón
    pygame.draw.rect(pantalla, color_boton , rectangulo)

    # Dibujar el texto centrado
    texto_superficie = fuente.render(texto, True, color_texto)
    texto_rectangulo = texto_superficie.get_rect(center=rectangulo.center)
    pantalla.blit(texto_superficie, texto_rectangulo)
    return rectangulo



