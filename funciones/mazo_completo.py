import random
import pygame


# espacio_entre_cartas = 15

# Función para repartir cartas
def repartir_cartas(mazo : list, cantidad : int) -> list:
    '''
    Reparte una cantidad específica de cartas desde el mazo
    Recibe un mazo de cartas y la cantidad a repartir
    Devuelve una determinada cantidad de cartas aleatorias
    '''
    cartas_mezcladas = random.sample(mazo, cantidad)  # Se seleccionan cartas aleatorias sin repetirse
    for carta in cartas_mezcladas:
        mazo.remove(carta)  # Eliminamos las cartas seleccionadas del mazo
    return cartas_mezcladas

def designar_posiciones(cartas : list, coordenadas_iniciales : int, espacio : int, tamaño_carta : tuple):
    '''
    Asigna posiciones y áreas de interacción a una lista de cartas
    Recibe una lista de cartas, una coordenada, un espacio de pixeles y un tamaño de la carta 
    '''
    x, y = coordenadas_iniciales # Posiciones iniciales de las cartas 
    for carta in cartas:
        
        carta["x"] = x # Se asignan posiciones nuevas a las cartas
        carta["y"] = y
        carta["rectangulo"] = pygame.Rect(x, y, tamaño_carta[0], tamaño_carta[1])  # Rectángulo para definir el área de interacción de la carta.
        x += tamaño_carta[0] + espacio # Actualiza la posición x para la próxima carta, dejando un espacio.




