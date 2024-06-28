import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *
import constantes

pygame.init()
ventana = pygame.display.set_mode(constantes.DIMENCIONES)
pygame.display.set_caption("¿Quién quiere ser millonario?")
fuente_reloj = pygame.font.SysFont('arialblack', 60)


# Cargar pregunta
imagenes_preguntas = []
for i in range(1, 17):
    imagen_path = f"imagenes/{i}.png"
    imagen = pygame.image.load(imagen_path)
    imagen = pygame.transform.scale(imagen, constantes.DIMENCIONES)
    imagenes_preguntas.append(imagen)
    
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
indice_pregunta = 0  # Índice de la pregunta actual
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta) # cargar la primer pregunta
x_ventana_izquierda = 0
x_ventana_derecha = constantes.ANCHO // 2
# Banderas 
bandera = True
jugar = False
ranking = False
mostrar_botones = True
bandera_jugar = False
tiempo_inicializado = False
game_over = False
resultado_opcion = "correcta"
retirarse = False

# Inicializar el tiempo y el reloj
tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
tiempo = pygame.time.Clock()

while bandera == True:  # bucle infinito para que se repita la pantalla
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        print(evento)
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            raton_x, raton_y = evento.pos
            
            if jugar == "JUGAR" and game_over == False and not retirarse:
                opciones = ["A", "B", "C", "D"]
                coordenadas_botones = {
                    "A": (constantes.BOTON_AX, constantes.BOTON_AY),
                    "B": (constantes.BOTON_BX, constantes.BOTON_BY),
                    "C": (constantes.BOTON_CX, constantes.BOTON_CY),
                    "D": (constantes.BOTON_DX, constantes.BOTON_DY)
                }
                
                alguna_correcta = False
                
                for opcion in opciones:
                    coordenadas_x, coordenadas_y = coordenadas_botones[opcion]
                    resultado = presionar_boton(coordenadas_x, coordenadas_y, opcion, raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    
                    if resultado == "CORRECTA":
                        premio = lista_premios[indice_pregunta]
                        print(premio)
                        indice_pregunta += 1
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                        alguna_correcta = True
                        resultado_opcion = "siguiente"
                        break
                    elif resultado == "INCORRECTA":
                        resultado_opcion = "incorrecta"        
                
                if alguna_correcta and indice_pregunta < len(lista_preguntas):
                    pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)   
        
            else:
                if mostrar_botones == True:
                    jugar = presionar_boton(constantes.BOTON_PLAY_X, constantes.BOTON_PLAY_Y, "JUGAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    ranking = presionar_boton(constantes.BOTON_RANKINX, constantes.BOTON_RANKINY, "RANKING", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                  
                    
    # Dibujar elementos en la ventana
    ventana.fill(colores.NEGRO)  # Rellenar la pantalla con un color
    
    if mostrar_botones == True:
        ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
        ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))
        ventana.blit(fondo_botones, (10, 460))
    
    if jugar == "JUGAR" or ranking == "RANKING":
        
        if x_ventana_izquierda > -600:
            x_ventana_izquierda -= constantes.VELOCIDAD
            x_ventana_derecha += constantes.VELOCIDAD
        elif tiempo_inicializado == False:
            tiempo_inicial = pygame.time.get_ticks()  # Inicializar el tiempo cuando las cortinas se han movido completamente
            tiempo_inicializado = True
            
    if x_ventana_derecha >= constantes.ANCHO :
        if ranking == "RANKING":
            mostrar_botones = False
            game_over = True
            ventana.blit(fondo_ranking, (0, 0))
            reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
            if reinicio == "REINICIAR":
                        ranking = False
                        jugar = False
                        mostrar_botones = True
                        x_ventana_izquierda = 0
                        x_ventana_derecha = constantes.ANCHO // 2
                        tiempo_inicializado = False
                        game_over = False
                        resultado_opcion = "correcta"
                        retirarse = False
                        indice_pregunta = 0
                        pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                        
        elif jugar == "JUGAR":
            if resultado_opcion == "incorrecta" or tiempo_restante == 0:
                mostrar_botones = False
                game_over = True
                ventana.blit(fondo_game_over, (0, 0))
                
                if game_over == True:
                    reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    if reinicio == "REINICIAR":
                        jugar = False
                        mostrar_botones = True
                        x_ventana_izquierda = 0
                        x_ventana_derecha = constantes.ANCHO // 2
                        tiempo_inicializado = False
                        game_over = False
                        resultado_opcion = "correcta"
                        retirarse = False
                        indice_pregunta = 0
                        pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                                
            elif resultado_opcion == "retirarse":
                mostrar_botones = False
                game_over = True
                ventana.blit(fondo_retiro, (0, 0))
                reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                if reinicio == "REINICIAR":
                    jugar = False
                    mostrar_botones = True
                    x_ventana_izquierda = 0
                    x_ventana_derecha = constantes.ANCHO // 2
                    tiempo_inicializado = False
                    game_over = False
                    resultado_opcion = "correcta"
                    retirarse = False
                    indice_pregunta = 0
                    pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                    tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                
            
            else:
                if resultado_opcion == "siguiente":  
                    ventana.blit((imagenes_preguntas[indice_pregunta]),(0,0))  
                    continuar = presionar_boton(constantes.BOTON_CONTINUARX, constantes.BOTON_CONTINUARY, "CONTINUAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    retirarse = presionar_boton(constantes.BOTON_RETIROX, constantes.BOTON_RETIROY, "RETIRARSE", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    if continuar == "CONTINUAR":
                        resultado_opcion = "correcta"
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)   
                    elif retirarse == "RETIRARSE":
                        resultado_opcion = "retirarse"  
                    elif indice_pregunta == 15:  
                        reiniciar = presionar_boton(constantes.REINICIO_FINX, constantes.REINICIO_FINY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                        if reiniciar == "REINICIAR" :
                            jugar = False
                            mostrar_botones = True
                            x_ventana_izquierda = 0
                            x_ventana_derecha = constantes.ANCHO // 2
                            tiempo_inicializado = False
                            game_over = False
                            resultado_opcion = "correcta"
                            retirarse = False
                            indice_pregunta = 0
                            pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                            tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                               
                           
                
                else:
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
