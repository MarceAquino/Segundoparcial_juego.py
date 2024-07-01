import pygame
import colores
import constantes
from lectura_escritura import *



lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
#----------------------------------------------------------------------------------------------------------------------------------------------------
def presionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y: int, opcion_correcta: str, opciones: dict) -> str:
    
    """ 
    Maneja la lógica al presionar un botón.

    Argumentos:
    - coordenadas_x: Tupla con las coordenadas X del botón.
    - coordenadas_y: Tupla con las coordenadas Y del botón.
    - boton: Nombre del botón.
    - raton_x: Coordenada X del ratón.
    - raton_y: Coordenada Y del ratón.
    - opcion_correcta: Opción correcta de la pregunta.
    - opciones: Diccionario de opciones de la pregunta.
    Retorna:
    - str: Mensaje que indica la acción realizada. """
    
    mensaje = ""
    if coordenadas_x[0] <= raton_x <= coordenadas_x[1] and coordenadas_y[0] <= raton_y <= coordenadas_y[1]:
        
        sonido_click = pygame.mixer.Sound(lista_sonido[1])
        sonido_click.set_volume(0.35)
        sonido_click.play()

        if boton in ["JUGAR", "RANKING", "CONTINUAR", "RETIRARSE", "REINICIAR"]:
            mensaje = boton
        
        else:
            # Verificar si la opción seleccionada es correcta
            if opciones[boton] == opcion_correcta:
                sonido_win = pygame.mixer.Sound(lista_sonido[4])
                sonido_win.set_volume(0.35)
                sonido_win.play()
                mensaje = "CORRECTA"
            else:
                sonido_loser = pygame.mixer.Sound(lista_sonido[2])
                sonido_loser.set_volume(0.35)
                sonido_loser.play()
                mensaje = "INCORRECTA"
    return mensaje
#----------------------------------------------------------------------------------------------------------------------------------------------------
def reiniciar_juego() -> tuple:
    """
    Reinicia el estado del juego.

    Retorna: 
    - jugar (bool)
    - mostrar_botones_cortina (bool)
    - x_ventana_izquierda (int)
    - x_ventana_derecha (int)
    - tiempo_inicializado (bool)
    - resultado_opcion (bool)
    - retirarse (bool)
    - indice_pregunta (int)
    - indice_imagen (int)
    - pregunta_actual (dict)
    - tiempo_inicial (int)
    - tiempo_restante (int) """
    
    jugar = False
    mostrar_botones_cortina = True
    x_ventana_izquierda = 0
    x_ventana_derecha = constantes.ANCHO // 2
    tiempo_inicializado = False
    resultado_opcion = False
    retirarse = False
    indice_pregunta = 0
    indice_imagen = -1
    pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
    tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
    
    return (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
             resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
            tiempo_inicial, tiempo_restante)
#----------------------------------------------------------------------------------------------------------------------------------------------------    
def obtener_preguntas_opciones(lista_preguntas: list[dict], indice: int) -> dict:
    """
    Obtiene la pregunta y las opciones de respuesta para una pregunta específica.

    Argumentos:
    - lista_preguntas: Lista de diccionarios con las preguntas y opciones.
    - indice: Índice de la pregunta en la lista.

    Retorna:
    - dict: Diccionario con los renderizados de la pregunta y las opciones, que incluye:
        - pregunta (Surface)
        - opcion_a (Surface)
        - opcion_b (Surface)
        - opcion_c (Surface)
        - opcion_d (Surface)
        - opcion_correcta (str)
        - opciones (dict) """
        
    preguntas = lista_preguntas[indice]
    pregunta = preguntas.get("pregunta")
    opcion_a = preguntas.get("opcion_a")
    opcion_b = preguntas.get("opcion_b")
    opcion_c = preguntas.get("opcion_c")
    opcion_d = preguntas.get("opcion_d")
    
    opcion_correcta = preguntas.get("opcion_correcta")
    
    fuente_respuestas =  pygame.font.SysFont('arial', 16)
    fuente = pygame.font.SysFont("arial black", 22, 1)
    pregunta_render = fuente.render(pregunta, True, colores.BLANCO)
    opcion_a_render = fuente_respuestas.render(opcion_a, True, colores.BLANCO)
    opcion_b_render = fuente_respuestas.render(opcion_b, True, colores.BLANCO)
    opcion_c_render = fuente_respuestas.render(opcion_c, True, colores.BLANCO)
    opcion_d_render = fuente_respuestas.render(opcion_d, True, colores.BLANCO)
    
    return {
        "pregunta": pregunta_render,
        "opcion_a": opcion_a_render,
        "opcion_b": opcion_b_render,
        "opcion_c": opcion_c_render,
        "opcion_d": opcion_d_render,
        "opcion_correcta": opcion_correcta,
        "opciones": {
            "A": opcion_a,
            "B": opcion_b,
            "C": opcion_c,
            "D": opcion_d
        }
    }
#----------------------------------------------------------------------------------------------------------------------------------------------------      
def reiniciar_tiempo(ultimo_tiempo: int) -> tuple:
    """
    Reinicia el tiempo del juego.

    Argumentos:
    - ultimo_tiempo: Tiempo total permitido.

    Retorna:
    - tuple: Tiempo inicial y tiempo restante actualizados.
        - tiempo_inicial_actualizado (int)
        - tiempo_restante_actualizado (int)"""
        
    tiempo_inicial_actualizado = pygame.time.get_ticks()  # Reiniciar el tiempo
    tiempo_restante_actualizado = ultimo_tiempo
    return tiempo_inicial_actualizado, tiempo_restante_actualizado   


#---------------------------------------------------------------------------------------------------------------------------------------------------- 
def centrar_texto(texto: str, ancho: int) -> str:
    """
    Centra un texto dentro de un ancho determinado agregando espacios a ambos lados.

    Argumentos:
    - texto: El texto que se va a centrar.
    - ancho: El ancho total deseado para el texto centrado.

    Retorna:
    - str: El texto centrado dentro del ancho especificado."""
    
    espacios = ancho - len(texto)
    izquierda = espacios // 2
    derecha = espacios - izquierda
    return ' ' * izquierda + texto + ' ' * derecha
#---------------------------------------------------------------------------------------------------------------------------------------------------- 
def mostrar_lista_jugadores(ventana, lista: list[dict], area: tuple) -> bool:
    
    """
    Muestra una lista de jugadores en la pantalla del juego.

    Argumentos:
    - ventana: La ventana de Pygame donde se mostrará la lista.
    - lista: Una lista de diccionarios que contiene los datos de los jugadores.
    - area: Tupla con coordenadas (x, y, ancho, alto) del área donde se mostrará la lista.

    Retorna:
    - bool: True si se muestra la lista de jugadores, False si la lista está vacía."""
    
    mensaje = True
    if len(lista) == 0:
        mensaje = None
    
    fuente = pygame.font.SysFont('arial', 20)
    x_inicial, y_inicial, ancho_area, alto_area = area
    espacio_vertical = (alto_area + 50 - y_inicial) // len(lista)
    
    matriz_jugadores = [[""] * 2 for _ in range(len(lista))]
    indice = 0
    
    for i in range(len(matriz_jugadores)):
        for j in range(len(matriz_jugadores[i])):
            if indice < len(lista):
                jugador = lista[indice]
                if j == 0:
                    texto = f"Jugador Nº{jugador['ID']}"
                else:
                    texto = f"${jugador['premio']}"
                matriz_jugadores[i][j] = centrar_texto(texto, 20)
                if j == 1:  # Solo incrementar el índice después de agregar ambas columnas
                    indice += 1
    for i, fila in enumerate(matriz_jugadores):
        for j, texto in enumerate(fila):
            if texto.strip():
                texto_superficie = fuente.render(texto, True, colores.BLANCO)
                ventana.blit(texto_superficie, (x_inicial + j * 800, y_inicial + i * espacio_vertical))

    return mensaje
#----------------------------------------------------------------------------------------------------------------------------------------------------         
