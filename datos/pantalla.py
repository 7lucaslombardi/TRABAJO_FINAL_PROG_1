import pygame


ANCHO, ALTO = 800, 600

pygame.display.set_caption("Truco Argentino")

pantalla = pygame.display.set_mode((ANCHO, ALTO))

icono = pygame.image.load("icono_truco.png")
pygame.display.set_icon(icono)

imagen_mazo = pygame.image.load("imagen_mazo.png")
rectangulo_mazo = pygame.Rect(30, 430, 136, 162)

fondo = pygame.image.load("fondo_mesa.png")

