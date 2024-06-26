import pygame
import colores
def precionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y: int, opcion_correcta: str, opciones: dict) -> bool:
    mensaje = False
    if coordenadas_x[0] <= raton_x <= coordenadas_x[1] and coordenadas_y[0] <= raton_y <= coordenadas_y[1]:
        sonido_click = pygame.mixer.Sound(r"sonido\click.wav")
        sonido_click.set_volume(0.35)
        sonido_click.play()
        if boton == "JUGAR":
           mensaje = True
        else:
            # Verificar si la opción seleccionada es correcta
            if opciones[boton] == opcion_correcta:
                sonido_win = pygame.mixer.Sound(r"sonido\win.mp3")
                sonido_win.set_volume(0.35)
                sonido_win.play()
                mensaje = True
            else:
                sonido_loser = pygame.mixer.Sound(r"sonido\loser.mp3")
                sonido_loser.set_volume(0.35)
                sonido_loser.play()
                mensaje = ""
                
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
    
def reiniciar_tiempo(tiempo_inicial, ultimo_tiempo):
    
    tiempo_inicial_actualizado = pygame.time.get_ticks()  # Reiniciar el tiempo
    tiempo_restante_actualizado = ultimo_tiempo
    return tiempo_inicial_actualizado, tiempo_restante_actualizado   