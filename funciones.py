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

def calcular_temporizador(tiempo_inicial, ultimo_tiempo):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_restante = ultimo_tiempo - int(tiempo_transcurrido / 1000)
    
    if tiempo_restante < 0:
        tiempo_restante = 0 
    
    if tiempo_restante > 20:
        color = colores.NEGRO
    elif tiempo_restante > 10:
        color = colores.NARANJA
    elif tiempo_restante > 0:
        color = colores.ROJO
    else:
        tiempo_restante = 0  
        color = colores.ROJO
    
    tiempo_restante_str = str(tiempo_restante).zfill(2)
    return tiempo_restante_str, color

def dibujar_temporizador(ventana, fuente_reloj, tiempo_restante_str, color):
    temporizador = fuente_reloj.render(tiempo_restante_str, True, color)
    ventana.blit(temporizador, (237, 637))

