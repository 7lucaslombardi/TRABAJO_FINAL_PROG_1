import pygame
from datos.colores import NEGRO


def verificar_mano(lista_carta_jugador : list,lista_carta_maquina : list) -> tuple:
    mano_ganadas_jugador = 0
    mano_ganadas_maquina = 0
    manos_ganadas = []  # Lista para almacenar quién ganó cada mano
    
    for i in range(len(lista_carta_jugador)):
        carta_jugador = lista_carta_jugador[i] # Compara carta con carta 1 y 1 y asi repetidamente, las manos
        carta_maquina = lista_carta_maquina[i]
        
        if carta_jugador["valor_truco"] > carta_maquina["valor_truco"]:
            mano_ganadas_jugador += 1
            manos_ganadas.append("jugador")  # Gana jugador
        elif carta_maquina["valor_truco"] >  carta_jugador["valor_truco"]:
            mano_ganadas_maquina += 1
            manos_ganadas.append("maquina")  # Gana maquina
        else:
            manos_ganadas.append("empate")  

    # DESEMPATE
    # Se verifica si las 3 rondas fueron jugadas
    if len(manos_ganadas) == 3:
        # Si las rondas ganadas son iguales, verificamos el empate en las manos
        if mano_ganadas_jugador == mano_ganadas_maquina:
            # Verificar si la primera mano fue empate
            if manos_ganadas[0] == "empate":
                # Si la primera fue empate, ver la segunda mano
                if manos_ganadas[1] == "jugador":
                    mano_ganadas_jugador += 1  
                elif manos_ganadas[1] == "maquina":
                    mano_ganadas_maquina += 1 
                else:
                    # Si también hay empate en la segunda, decidir con la tercera mano
                    if manos_ganadas[2] == "jugador":
                        mano_ganadas_jugador += 1  
                    elif manos_ganadas[2] == "maquina":
                        mano_ganadas_maquina += 1  
            else:
                # Si la primera mano no fue empate, le asignamos la ronda al que ganó la primera mano
                if manos_ganadas[0] == "jugador":
                    mano_ganadas_jugador += 1  # El jugador gana la ronda por la primera mano
                else:
                    mano_ganadas_maquina += 1  # La maquina gana la ronda por la primera mano

    # Al final, devolvemos el marcador
    return mano_ganadas_jugador, mano_ganadas_maquina

def verificar_ganador_rondas(lista_carta_jugador : list, lista_carta_maquina : list,
                            puntos_jugador : int, puntos_maquina : int, terminar_ronda : bool) -> tuple:
    
    mano_ganadas_jugador, mano_ganadas_maquina = verificar_mano(
        lista_carta_jugador,lista_carta_maquina)
    
    puntos_a_sumar = 1 
    
    if mano_ganadas_jugador > mano_ganadas_maquina:
        puntos_jugador += puntos_a_sumar
    elif mano_ganadas_maquina > mano_ganadas_jugador:
        puntos_maquina += puntos_a_sumar
    elif terminar_ronda == True:
        puntos_maquina += puntos_a_sumar
    else:
        return 0

    return puntos_jugador, puntos_maquina







def cantar_truco(jugador, oponente):
    print(f"{jugador} canta Truco! ¿Aceptas? (sí/no)")
    respuesta = input()
    if respuesta.lower() == "sí":
        print(f"{oponente} responde Truco!")
        return True  # Se acepta el Truco
    else:
        print(f"{oponente} pierde la mano.")
        return False  # Oponente no acepta
    

def verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina):

    

    if (carta_jugador['valor_truco']) > (carta_maquina['valor_truco']):
        rondas_ganadas_jugador+= 1
    elif (carta_maquina['valor_truco']) > (carta_jugador['valor_truco']):
        rondas_ganadas_maquina += 1
    else:
        return 0
    
    return rondas_ganadas_jugador, rondas_ganadas_maquina




def verificar_rondas(rondas_ganadas_jugador, rondas_ganadas_maquina, puntos_jugador, puntos_maquina, puntos_a_sumar):
    
    if rondas_ganadas_jugador > rondas_ganadas_maquina:
        puntos_jugador += puntos_a_sumar
    elif rondas_ganadas_maquina > rondas_ganadas_jugador:
        puntos_maquina += puntos_a_sumar
    else:
        return 0

    return puntos_jugador, puntos_maquina






# Ranking para el truco
def ganar_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina, opcion_canto, opcion_rta):
    truco = "truco"
    retruco = "retruco"
    valecuatro = "valecuatro"
    quiero = "si"
    
    if truco == "truco":
        
        
        if quiero == "si":
            puntos_a_sumar = 2
            verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)

        elif quiero == "no":
            puntos_a_sumar = 1
            verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)
        
        elif retruco == "retruco":
            pass

            if quiero == "si":
                puntos_a_sumar = 3
                verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)

            elif quiero == "no":
                puntos_a_sumar = 2
                verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)

            elif valecuatro == "valecuatro":
                pass

                if quiero == "si":
                    puntos_a_sumar = 4
                    verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)

                else:
                    puntos_a_sumar = 3
                    verificar_cartas_jugadas_truco(carta_jugador, carta_maquina, rondas_ganadas_jugador, rondas_ganadas_maquina)

        

    
