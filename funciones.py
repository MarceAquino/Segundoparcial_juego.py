import pygame
import colores
from lectura_escritura import *

lista_preguntas = cargar_preguntas_csv("Preguntas.csv")


def presionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y: int, opcion_correcta: str, opciones: dict) -> str:
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

def reiniciar_juego():
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
    
def obtener_preguntas_opciones(lista_preguntas: list[dict], indice: int):
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
    
def reiniciar_tiempo(ultimo_tiempo):
    
    tiempo_inicial_actualizado = pygame.time.get_ticks()  # Reiniciar el tiempo
    tiempo_restante_actualizado = ultimo_tiempo
    return tiempo_inicial_actualizado, tiempo_restante_actualizado   



def guardar_jugador_premio(numero_jugador,premio,lista_ranking) -> list:
    
    premio = int(premio)
    jugador = {"jugador":numero_jugador,
                "premio":premio
                }
    if jugador not in lista_ranking:
        lista_ranking.append(jugador)
        
    return lista_ranking



