
estado_juego = {
    "cartas_jugador": [],
    "cartas_maquina": [],
    "lista_carta_jugador": [],
    "lista_carta_maquina": [],
    "ronda": 0,
    "puntos_jugador" : 0,
    "puntos_maquina" : 0,
    "turno_jugador": True,
    "turno_maquina": False,
    "terminar_ronda" : False
}


def reiniciar_juego(estado_juego : dict) -> None:

    estado_juego["cartas_jugador"] = []
    estado_juego["cartas_maquina"] = []
    estado_juego["lista_carta_jugador"] = []
    estado_juego["lista_carta_maquina"] = []
    estado_juego["ronda"] = 0
    estado_juego["puntos_jugador"] = 0
    estado_juego["puntos_maquina"] = 0
    estado_juego["turno_jugador"] = True
    estado_juego["turno_maquina"] = False

