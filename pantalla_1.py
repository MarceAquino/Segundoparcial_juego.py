import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *
import constantes

pygame.init()
ventana = pygame.display.set_mode(constantes.DIMENSIONES)
pygame.display.set_caption("¿Quién quiere ser millonario?")
fuente_reloj = pygame.font.SysFont('arialblack', 60)

# Cargar preguntas e imágenes
imagenes_preguntas = []
for i in range(1, 17):
    imagen_path = f"imagenes/{i}.png"
    imagen = pygame.image.load(imagen_path)
    imagen = pygame.transform.scale(imagen, constantes.DIMENSIONES)
    imagenes_preguntas.append(imagen)
    
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
indice_pregunta = 0
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
x_ventana_izquierda = 0
x_ventana_derecha = constantes.ANCHO // 2

# Banderas y estado del juego
bandera = True
jugar = False
ranking = False
mostrar_botones = True
tiempo_inicializado = False
game_over = False
retirarse = False

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
            
            if jugar == "JUGAR" and not game_over and not retirarse:
                opciones = ["A", "B", "C", "D"]
                coordenadas_botones = {
                    "A": (constantes.BOTON_AX, constantes.BOTON_AY),
                    "B": (constantes.BOTON_BX, constantes.BOTON_BY),
                    "C": (constantes.BOTON_CX, constantes.BOTON_CY),
                    "D": (constantes.BOTON_DX, constantes.BOTON_DY)
                }
                
                for opcion in opciones:
                    coordenadas_x, coordenadas_y = coordenadas_botones[opcion]
                    resultado = presionar_boton(coordenadas_x, coordenadas_y, opcion, raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    
                    if resultado == "CORRECTA":
                        indice_pregunta += 1
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                        if indice_pregunta < len(lista_preguntas):
                            pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                        break
                    elif resultado == "INCORRECTA":
                        game_over = True
                        mostrar_botones = False
                        ventana.blit(fondo_game_over, (0, 0))
                        break
                    elif resultado == "RETIRARSE":
                        retirarse = True
                        mostrar_botones = False
                        ventana.blit(fondo_retiro, (0, 0))
                        fuente = pygame.font.SysFont("arial", 20)
                        pygame.draw.rect(ventana, colores.NEGRO, (80, 50, 350, 100)) 
                        texto_premio = fuente.render(f"Usted se retiró con: ${lista_premios[indice_pregunta]}", True, colores.BLANCO)
                        ventana.blit(texto_premio, (100, 75))
                        break
                        
                if game_over or retirarse:
                    reinicio = presionar_boton(constantes.BOTON_REINICIARX, constantes.BOTON_REINICIARY, "REINICIAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    if reinicio == "REINICIAR":
                        jugar = False
                        ranking = False
                        mostrar_botones = True
                        x_ventana_izquierda = 0
                        x_ventana_derecha = constantes.ANCHO // 2
                        tiempo_inicializado = False
                        game_over = False
                        retirarse = False
                        indice_pregunta = 0
                        pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
                    
    ventana.fill(colores.NEGRO)
    
    if mostrar_botones:
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
            mostrar_botones = False
            game_over = False
            ventana.blit(fondo_ranking, (0, 0))
        elif jugar == "JUGAR" and game_over:
            ventana.blit(fondo_game_over, (0, 0))
        elif retirarse:
            ventana.blit(fondo_retiro, (0, 0))
            
    pygame.display.update()
    tiempo.tick(constantes.FPS)
