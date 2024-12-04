RUTA_ARCHIVO = "archivo/ranking.csv"  # Archivo donde se guardan los puntajes
from funciones.botones import crear_boton
from datos.colores import GRIS, NEGRO
from datos.pantalla import pantalla

def cargar_registros():
    """
    Carga los registros existentes desde el archivo csv
    """
    registro = {}
    with open(RUTA_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        next(archivo)  # Salta la primera linea
        for linea in archivo:
            nombre, partidas_ganadas = linea.strip().split(",")  # Separa por comas
            registro[nombre] = int(partidas_ganadas)  # Se guarda como {"nombre": partidas_ganadas}

    return registro


def mostrar_registros():

    registros = cargar_registros()
    y = 50
    crear_boton(pantalla, f"Nombre        -        Partidas ganadas", (280, y), (300, 30), GRIS, NEGRO, "impact", 36)

    for nombre in registros:
        
        y += 50
        partidas_ganadas = registros[nombre]
        crear_boton(pantalla, f"{nombre}        -        {partidas_ganadas}", (300, y), (150, 30), GRIS, NEGRO, "comicsansms", 22)
        


def guardar_partidas(registros : dict) -> None:
    """
    Guarda los registros en el archivo csv 
    Recibe un diccionario de registros
    """
    with open(RUTA_ARCHIVO, mode="w", encoding="utf-8") as archivo:
        archivo.write("Nombre, Partidas ganadas\n")  # Escribir la cabecera nuevamente
        for nombre in registros:  # Recorre las claves del diccionario
                partidas_ganadas = registros[nombre]  # Obtiene el valor asociado a esa clave
                archivo.write(f"{nombre},{partidas_ganadas}\n")  # Escribe en el archivo


def verificar_jugador(nombre : str) -> None:
    """
    Verifica si el jugador ya existe y muestra su puntaje, sino lo guarda
    """
    registros = cargar_registros()  # Cargar puntuaciones desde el archivo
    
    if nombre in registros:
        print(f"¡{nombre}! Tu ranking de partidas ganadas es: {registros[nombre]}")
    else:
        print(f"¡Bienvenido, {nombre}! Eres un nuevo jugador.")
        registros[nombre] = 0  # Asignar puntaje inicial al nuevo jugador
        guardar_partidas(registros)  # Guardar el nuevo jugador en el archivo

def actualizar_partidas(nombre : str, partida : int = 1) -> None:
    """
    Suma el puntaje total del jugador en todas sus partidas jugadas
    """
    partidas = cargar_registros()
    
    if nombre in partidas:
        partidas[nombre] += partida 
        
    else:
        partidas[nombre] = partida   # Agrega nuevo jugador
        
    
    guardar_partidas(partidas)





