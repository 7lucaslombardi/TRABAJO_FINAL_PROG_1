from funciones.imagen_cartas import *
from funciones.mazo_completo import *


fondo = pygame.image.load("fondo_mesa.png")

def nueva_ronda(estado_juego : dict, mazo : list, pantalla):
    """
    Inicia las variables para empezar la ronda
    Recibe un diccionario especifico, una lista de cartas y la pantalla
    """
    estado_juego["cartas_jugador"] = repartir_cartas(mazo, 3)
    estado_juego["cartas_maquina"] = repartir_cartas(mazo, 3)
    estado_juego["lista_carta_jugador"] = []
    estado_juego["lista_carta_maquina"] = []

    designar_posiciones(estado_juego["cartas_maquina"], coordenadas_maquina, 15, TAMAÑO_CARTA)
    designar_posiciones(estado_juego["cartas_jugador"], coordenadas_jugador, 15, TAMAÑO_CARTA)
    pantalla.blit(fondo, (0, 0)) # Redibuja la pantalla

    estado_juego["turno_jugador"] = estado_juego["ronda"] % 2 == 0
    estado_juego["turno_maquina"] = not estado_juego["turno_jugador"]
    estado_juego["ronda"] += 1
