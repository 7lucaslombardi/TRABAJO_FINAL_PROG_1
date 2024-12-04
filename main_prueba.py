from datos.info_cartas import *
from datos.colores import * 
from funciones import *
from prueba_juego import mazo
import random


def juego_completo(mazo):


    cartas_jugador = repartir_cartas(mazo, 3)
    cartas_maquina = repartir_cartas(mazo, 3)
    print(cartas_jugador)
    print(cartas_maquina)

    rondas_ganadas_jugador = 0
    rondas_ganadas_maquina = 0
    
    ronda_1 = verificar_cartas_jugadas_truco(cartas_jugador[0], cartas_maquina[0], rondas_ganadas_jugador, rondas_ganadas_maquina)
    rondas_ganadas_jugador, rondas_ganadas_maquina = ronda_1

    ronda_2 = verificar_cartas_jugadas_truco(cartas_jugador[1], cartas_maquina[1], rondas_ganadas_jugador, rondas_ganadas_maquina)
    rondas_ganadas_jugador, rondas_ganadas_maquina = ronda_2


    ronda_3 = verificar_cartas_jugadas_truco(cartas_jugador[2], cartas_maquina[2], rondas_ganadas_jugador, rondas_ganadas_maquina)
    

    print(ronda_1)
    print(ronda_2)
    print(ronda_3)



juego_completo(mazo)