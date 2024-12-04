import pygame
import time



# Inicializar Pygame
pygame.init()
from datos import *
from funciones import *
pygame.mixer.init()


# Cargar imágenes directamente en el diccionario de cada carta
for carta in mazo_original:
    imagen_original = pygame.image.load(carta["ruta"])
    carta["imagen"] = pygame.transform.scale(imagen_original, TAMAÑO_CARTA)  # Redimensionar

clock = pygame.time.Clock()


# Bucle principal del juego
ejecutar_juego = True
clock = pygame.time.Clock()
nombre_ingresado = ""
nombre_enviado = False
MAXIMO_PUNTOS = 2
musica_sonando = False


opcion = 1


while ejecutar_juego:
    
    
    match opcion:
        case 1: 
            
            if not musica_sonando:  # Solo cargar y reproducir si no está sonando
                pygame.mixer.music.load("sonido_inicio.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1)
                musica_sonando = True
            
            # pantalla de inicio 
            pantalla.fill(ROJO)
            crear_boton(pantalla, "BIENVENIDOS AL TRUCO ARGENTINO", (200, 100), (400, 30), ROJO, NEGRO, "impact", 36 )
            boton_nuevo_juego = crear_boton(pantalla, "NUEVO JUEGO", (330, 450), (140, 30), BLANCO, NEGRO, "comicsansms", 18)
            boton_ranking = crear_boton(pantalla, "RANKING", (330, 500), (140, 30), BLANCO, NEGRO, "comicsansms", 18)
            
            crear_boton(pantalla, nombre_ingresado.capitalize(), (200, 200), (300, 30), BLANCO, NEGRO, "comicsansms", 17)
            rectangulo_boton_guardar = crear_boton(pantalla, "GUARDAR", (520, 200),(100, 30)
                                    , BLANCO if not nombre_enviado else GRIS, NEGRO, "comicsansms", 20)
            
            texto_puntos = crear_boton(pantalla, "Puntos a jugar :", (150, 347), (120, 30), ROJO, NEGRO, "impact", 20)
            boton_puntos_15 = crear_boton(pantalla, "15 PUNTOS", (300, 350), (100, 30)
                                        , BLANCO if not MAXIMO_PUNTOS == 2 else GRIS, NEGRO, "comicsansms", 16)
            boton_puntos_30 = crear_boton(pantalla, "30 PUNTOS", (450, 350), (100, 30)
                                        , BLANCO if not MAXIMO_PUNTOS == 30  else GRIS, NEGRO, "comicsansms", 16)


            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    ejecutar_juego = False

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if not nombre_enviado and rectangulo_boton_guardar.collidepoint(evento.pos):
                        if nombre_ingresado.strip():  # Enviar nombre solo si no está vacío
                            
                            verificar_jugador(nombre_ingresado.capitalize())
                            nombre_enviado = True

                if evento.type == pygame.KEYDOWN and not nombre_enviado: # Una vez que se pisa guardar no deja borrar el texto
                    if evento.key == pygame.K_BACKSPACE:
                        nombre_ingresado = nombre_ingresado[:-1] # Va borrando el ultimo caracter
                    elif len(nombre_ingresado) < 20:  # Limite de caracteres
                        nombre_ingresado += evento.unicode # Va guardando el texto

                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if boton_nuevo_juego.collidepoint(evento.pos) and nombre_enviado == True:
                        opcion = 2
                        pygame.mixer.music.stop()  # Detiene la música
                        musica_sonando = False

                
                    elif boton_puntos_15.collidepoint(evento.pos):
                        
                        MAXIMO_PUNTOS = 2
                        
                    elif boton_puntos_30.collidepoint(evento.pos):
                        
                        MAXIMO_PUNTOS = 30

                    elif boton_ranking.collidepoint(evento.pos):
                        
                        opcion = 4
                        
            pygame.display.update()
        
        case 2:
            #   logica del juego                                         
            # Inicializar la primera ronda
            if estado_juego["ronda"] == 0:
                nueva_ronda(estado_juego, mazo_original, pantalla)
                redibujar_pantalla(pantalla, estado_juego["cartas_jugador"], estado_juego["lista_carta_jugador"]
                                , estado_juego["lista_carta_maquina"], estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] )

            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    ejecutar_juego = False
                    
            # Verifico evento Mouse
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    # Movimientos del jugador
                    if estado_juego["turno_jugador"]:
                        for carta in estado_juego["cartas_jugador"]:
                            if carta["rectangulo"].collidepoint(evento.pos):
                                
                                    # Se agrega la carta seleccionada a la lista nueva y se elimina de las tres cartas
                                    estado_juego["lista_carta_jugador"].append(carta)
                                    estado_juego["cartas_jugador"].remove(carta)
                                    
                                    redibujar_pantalla(pantalla, estado_juego["cartas_jugador"], estado_juego["lista_carta_jugador"]
                                                    , estado_juego["lista_carta_maquina"], estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] )
                                    
                                    # Rectangulos de las cartas con posiciones
                                    designar_posiciones(estado_juego["cartas_jugador"], coordenadas_jugador, espacio_entre_cartas, TAMAÑO_CARTA)
                                    estado_juego["turno_jugador"] = False
                                    estado_juego["turno_maquina"] = True
                                    break
                            
                            elif rectangulo_mazo.collidepoint(evento.pos):

                                estado_juego["terminar_ronda"] = True 


            
            # Movimientos de la maquina
            if estado_juego["turno_maquina"]:
                for carta_lanzada_maquina in estado_juego["cartas_maquina"]: 
                    
                        time.sleep(1)
                        # Se agrega la carta seleccionada a la lista nueva y se elimina de las tres cartas
                        estado_juego["lista_carta_maquina"].append(carta_lanzada_maquina)
                        estado_juego["cartas_maquina"].remove(carta_lanzada_maquina)
                        
                        redibujar_pantalla(pantalla, estado_juego["cartas_jugador"], estado_juego["lista_carta_jugador"]
                                        , estado_juego["lista_carta_maquina"], estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] )
                        
                        # Posiciones de las cartas sobre la mesa de la maquina a medida que va tirando
                        designar_posiciones(estado_juego["cartas_jugador"], coordenadas_jugador, espacio_entre_cartas, TAMAÑO_CARTA)

                        estado_juego["turno_jugador"] = True
                        estado_juego["turno_maquina"] = False
                
                        break

            
            # Se verifica si se jugaron las tres cartas de cada uno y arranca una nueva ronda
            if  (estado_juego["cartas_jugador"] == [] and estado_juego["cartas_maquina"] == []) or estado_juego["terminar_ronda"] == True:
                estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] = verificar_ganador_rondas(estado_juego["lista_carta_jugador"], estado_juego["lista_carta_maquina"], 
                                        estado_juego["puntos_jugador"], estado_juego["puntos_maquina"], estado_juego["terminar_ronda"])
                estado_juego["terminar_ronda"] = False
                time.sleep(1)
                nueva_ronda(estado_juego,mazo_original,pantalla)
                redibujar_pantalla(pantalla, estado_juego["cartas_jugador"], estado_juego["lista_carta_jugador"]
                                , estado_juego["lista_carta_maquina"], estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] )
                
            
            if estado_juego["puntos_jugador"] == MAXIMO_PUNTOS or estado_juego["puntos_maquina"] == MAXIMO_PUNTOS:
                
                redibujar_pantalla(pantalla, estado_juego["cartas_jugador"], estado_juego["lista_carta_jugador"]
                                , estado_juego["lista_carta_maquina"], estado_juego["puntos_jugador"], estado_juego["puntos_maquina"] )
                time.sleep(0.5)

                opcion = 3


        case 3:
            
            boton_menu_principal = crear_boton(pantalla, "MENU PRINCIPAL", (200, 400), (170, 30), BLANCO, NEGRO, "comicsansms", 16)
            boton_volver_a_jugar = crear_boton(pantalla, "VOLVER A JUGAR ", (400, 400), (170, 30), BLANCO, NEGRO, "comicsansms", 16)

            if estado_juego["puntos_jugador"] > estado_juego["puntos_maquina"]:
                pantalla.fill(VERDE)
                crear_boton(pantalla, f"Felicidades {nombre_ingresado.capitalize()} has ganado!!!", (200, 100), (400, 30), VERDE, NEGRO, "impact", 36)
                actualizar_partidas(nombre_ingresado.capitalize())
            elif estado_juego["puntos_jugador"] < estado_juego["puntos_maquina"]:
                pantalla.fill(VERDE)
                crear_boton(pantalla, f"Malas noticias {nombre_ingresado.capitalize()} has perdido!!!", (200, 100), (400, 30), VERDE, NEGRO, "impact", 36)
            pygame.display.update()
            
            reiniciar_juego(estado_juego) # Actualiza todo el diccionario desde 0
            
            
            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    ejecutar_juego = False
                    
            # Verifico evento Mouse
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if boton_menu_principal.collidepoint(evento.pos):
                        nombre_ingresado = ""
                        nombre_enviado = False
                        opcion = 1
                    elif boton_volver_a_jugar.collidepoint(evento.pos):
                        opcion = 2

        case 4:
            pantalla.fill(GRIS)
            
            mostrar_registros()
            boton_menu_principal = crear_boton(pantalla, "MENU PRINCIPAL", (50, 500), (170, 30), BLANCO, NEGRO, "comicsansms", 16)

            for evento in pygame.event.get():
                
                if evento.type == pygame.QUIT:
                    ejecutar_juego = False

                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if boton_menu_principal.collidepoint(evento.pos):
                        nombre_ingresado = ""
                        nombre_enviado = False
                        opcion = 1

            

        
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            ejecutar_juego = False
    
    clock.tick(30)
    pygame.display.update()

# Salir de Pygame
pygame.quit()
