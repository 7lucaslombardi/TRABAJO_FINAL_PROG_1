import random
from funciones.envido import *

def jugador_aleatorio(cartas):
    
    jugada = lambda cartas: random.choice(cartas)  # Juega una carta al azar
    # Cantar Falta Envido si tiene más de 30 puntos
    # envido_puntos = envido(cartas)
    # if envido_puntos > 30:  # Si tiene más de 30 puntos, canta "Falta Envido"
    #     print("Canta 'Falta Envido'")
    
    return jugada


def jugador_estrategico(cartas, puntos, turno):
    cartas.sort(key=lambda x: x.valor, reverse=True)  # Ordenamos las cartas de mayor a menor
    
    if turno == 1:  # Si es el primer jugador
        jugada = cartas[0]  # Juega la carta más alta
    else:
        # Juega la carta que pueda ganar o empatar 
        jugada = cartas[0] if puntos > 27 else cartas[-1]
    
    # Cantar Envido si tiene más de 27 puntos
    envido_puntos = envido(cartas)
    if envido_puntos > 27:  # Solo canta Envido si tiene más de 27 puntos
        print("Canta 'Envido'")
    
    return jugada
