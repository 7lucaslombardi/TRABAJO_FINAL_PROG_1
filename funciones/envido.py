from datos.colores import NEGRO
import pygame

# rect_boton_envido = pygame.Rect((700, 250, 100, 30))
# fuente = pygame.font.Font(None, 24)
# texto = fuente.render("ENVIDO", True, NEGRO)


def calcular_envido(carta1, carta2):
    if carta1.palo == carta2.palo:
        puntos = carta1.valor + carta2.valor
        if puntos > 20:
            puntos -= 20
        return puntos
    return 0  # No se puede hacer envido si las cartas no tienen el mismo palo

def envido(cartas):
    # Ordenamos las cartas por palo y valor
    cartas_palo = {}
    for carta in cartas:
        if carta.palo not in cartas_palo:
            cartas_palo[carta.palo] = []
        cartas_palo[carta.palo].append(carta)

    # Buscar la mejor combinación de envido
    mejor_envido = 0
    for palo, cartas_palo in cartas_palo.items():
        if len(cartas_palo) > 1:
            for i in range(len(cartas_palo)):
                for j in range(i + 1, len(cartas_palo)):
                    envido_actual = calcular_envido(cartas_palo[i], cartas_palo[j])
                    if envido_actual > mejor_envido:
                        mejor_envido = envido_actual
    
    return mejor_envido














