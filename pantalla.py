import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *
import constantes
import json

pygame.init()
ventana = pygame.display.set_mode(constantes.DIMENSIONES)
pygame.display.set_caption("¿Quién quiere ser millonario?")
fuente_reloj = pygame.font.SysFont('arialblack', 60)
# Cargar imágenes de preguntas
imagenes_preguntas = cargar_imagenes(lista_imagenes)


# Cargar preguntas desde un archivo CSV
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
indice_pregunta = 0
indice_imagen = -1
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
x_ventana_izquierda = 0
x_ventana_derecha = constantes.ANCHO // 2

# Inicialización de banderas y variables de juego
lista_ranking = []
bandera = True
jugar = False
ranking = False
mostrar_botones_cortina = True
mostrar_botones_opciones = False
bandera_jugar = False
tiempo_inicializado = False
resultado_opcion = False
retirarse = False
id_jugador = 1

# Inicializar el tiempo y el reloj
tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
tiempo = pygame.time.Clock()

while bandera:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            raton_x, raton_y = evento.pos
            
            if jugar == "JUGAR" and retirarse != "RETIRARSE"  :
               
                
                opciones = ["A", "B", "C", "D"]
                coordenadas_botones = {
                    "A": (constantes.BOTON_AX, constantes.BOTON_AY),
                    "B": (constantes.BOTON_BX, constantes.BOTON_BY),
                    "C": (constantes.BOTON_CX, constantes.BOTON_CY),
                    "D": (constantes.BOTON_DX, constantes.BOTON_DY)
                }
                if mostrar_botones_opciones:
                    for opcion in opciones:
                        coordenadas_x, coordenadas_y = coordenadas_botones[opcion]
                        resultado = presionar_boton(coordenadas_x, coordenadas_y, opcion, raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                        
                        if resultado == "CORRECTA":
                            retirarse = False
                            premio = lista_premios[indice_pregunta]
                            premio = str(premio)
                            tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                            resultado_opcion = "siguiente"
                            indice_imagen += 1
                            indice_pregunta += 1
                            break
                        elif resultado == "INCORRECTA":
                            resultado_opcion = "incorrecta"
                            mostrar_botones_opciones = False
                    
                    if indice_pregunta < len(lista_preguntas):
                        pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
            
            else:
                if mostrar_botones_cortina:
                    jugar = presionar_boton(constantes.BOTON_PLAY_X, constantes.BOTON_PLAY_Y, "JUGAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    ranking = presionar_boton(constantes.BOTON_RANKINX, constantes.BOTON_RANKINY, "RANKING", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
    
    
    ventana.fill(colores.NEGRO)
    
    if mostrar_botones_cortina:
        ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
        ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))
        ventana.blit(fondo_botones, (10, 460))
    
    if jugar == "JUGAR" or ranking == "RANKING":
        
        if x_ventana_izquierda > -600:
            x_ventana_izquierda -= constantes.VELOCIDAD
            x_ventana_derecha += constantes.VELOCIDAD
        elif not tiempo_inicializado:
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_inicializado = True
    
            
    if x_ventana_derecha >= constantes.ANCHO:
        if ranking == "RANKING":
            mostrar_botones_cortina = False
            ventana.blit(fondo_ranking, (0, 0))
            reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
            if reinicio == "REINICIAR":
                ranking = False
                (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
                 resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
                tiempo_inicial, tiempo_restante) = reiniciar_juego()
                tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                
        elif jugar == "JUGAR":
            
            if resultado_opcion == "incorrecta":
                mostrar_botones_cortina = False
                ventana.blit(fondo_game_over, (0, 0))
                reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                if reinicio == "REINICIAR":
                    (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
                     resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
                    tiempo_inicial, tiempo_restante) = reiniciar_juego()
                    
            elif tiempo_restante == 0:       
                mostrar_botones_cortina = False
                ventana.blit(fondo_game_over, (0, 0))
                reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                if reinicio == "REINICIAR":
                    (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
                     resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
                    tiempo_inicial, tiempo_restante) = reiniciar_juego()    
                                
            elif resultado_opcion == "retirarse":
                mostrar_botones_cortina = False
                ventana.blit(fondo_retiro, (0, 0))
                reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                fuente = pygame.font.SysFont("arial", 24)
                pygame.draw.rect(ventana, colores.FONDO, (80, 50, 350, 100)) 
                texto_jugador = fuente.render(f"Usted es el jugador numero: {id_jugador} ", True, colores.BLANCO)
                texto_premio = fuente.render(f"Se retiró con un premio de: ${premio} ", True, colores.BLANCO)
                ventana.blit(texto_jugador,(100,60))
                ventana.blit(texto_premio, (100, 80))
                if reinicio == "REINICIAR":
                    print(guardar_jugador_premio(id_jugador,premio,lista_ranking))
                    id_jugador += 1  
                    (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
                     resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
                    tiempo_inicial, tiempo_restante) = reiniciar_juego()
            
            else:
                if resultado_opcion == "siguiente":  
                    mostrar_botones_opciones = False
                    ventana.blit(imagenes_preguntas[indice_imagen], (0, 0))  
                    continuar = presionar_boton(constantes.BOTON_CONTINUARX, constantes.BOTON_CONTINUARY, "CONTINUAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    retirarse = presionar_boton(constantes.BOTON_RETIROX, constantes.BOTON_RETIROY, "RETIRARSE", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    if continuar == "CONTINUAR":
                        resultado_opcion = False
                        mostrar_botones_opciones = True           
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)   
                    elif retirarse == "RETIRARSE":
                        resultado_opcion = "retirarse"  
                    elif indice_pregunta == 15:  
                        mostrar_botones_opciones = False
                        ventana.blit(fondo_ganador, (0,0))
                        reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                        if reinicio == "REINICIAR":
                            print(guardar_jugador_premio(id_jugador,premio,lista_ranking))
                           
                            id_jugador += 1 
                            (jugar, mostrar_botones_cortina, x_ventana_izquierda, x_ventana_derecha, tiempo_inicializado,
                             resultado_opcion, retirarse, indice_pregunta,indice_imagen, pregunta_actual,
                            tiempo_inicial, tiempo_restante) = reiniciar_juego()
                
                else:
                    mostrar_botones_opciones = True
                    ventana.blit(fondo_preguntas, (0, 0))
                    ventana.blit(pregunta_actual["pregunta"], (280, 60))
                    ventana.blit(pregunta_actual["opcion_a"], (365, 210))
                    ventana.blit(pregunta_actual["opcion_b"], (365, 265))
                    ventana.blit(pregunta_actual["opcion_c"], (665, 210))
                    ventana.blit(pregunta_actual["opcion_d"], (665, 265))
                    
                    # Calcular el tiempo transcurrido y restante
                    tiempo_actual = pygame.time.get_ticks()
                    tiempo_transcurrido = tiempo_actual - tiempo_inicial
                    tiempo_restante = constantes.ULTIMO_TIEMPO - int(tiempo_transcurrido / 1000)
                    get_color = lambda tiempo_restante: colores.NEGRO if tiempo_restante > 20 else (colores.NARANJA if tiempo_restante > 10 else colores.ROJO)
                    tiempo_restante = max(tiempo_restante, 0)
                    color = get_color(tiempo_restante)
                    tiempo_restante_str = str(tiempo_restante).zfill(2)
                    temporizador = fuente_reloj.render(tiempo_restante_str, True, color)
                    ventana.blit(temporizador, (237, 637))
    
    pygame.display.update()  # Actualizar la pantalla
