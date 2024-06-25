import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *

pygame.init()

# Configuración de ventana
ANCHO = 1200
ALTO = 800
DIMENCIONES = (ANCHO, ALTO)
ventana = pygame.display.set_mode(DIMENCIONES) # pixeles ancho x largo
pygame.display.set_caption("¿Quién quiere ser millonario?") # título de la ventana
imagen = pygame.image.load("imagenes/icon.png") # método load carga una imagen devuelve una superficie
pygame.display.set_icon(imagen) # pongo la imagen como icono en la ventana
fuente_reloj = pygame.font.SysFont('arialblack', 60)

# Constantes
FPS = 30
VELOCIDAD = 3

# Inicializar el tiempo y el reloj
ultimo_tiempo = 30  
tiempo_inicial = 0
tiempo_restante = ultimo_tiempo
tiempo = pygame.time.Clock()

# Fondo
# Cargar y escalar la imagen de fondo
fondo_cortina_izquierda = pygame.image.load(r"imagenes/fondo_cortina.png")
fondo_cortina_izquierda = pygame.transform.scale(fondo_cortina_izquierda, (ANCHO // 2, ALTO))
fondo_cortina_derecha = pygame.image.load(r"imagenes/fondo_cortina.png")
fondo_cortina_derecha = pygame.transform.scale(fondo_cortina_izquierda, (ANCHO // 2, ALTO))
fondo_cortina_derecha = pygame.transform.flip(fondo_cortina_derecha, True, False)
fondo_botones = pygame.image.load(r"imagenes/fondo_menu.png")
fondo_preguntas = pygame.image.load(r"imagenes/fondo1_preguntas.png")
fondo_preguntas = pygame.transform.scale(fondo_preguntas, DIMENCIONES)
fondo_game_over = pygame.image.load(r"imagenes\fondo3_incorrecto.png")

imagenes_preguntas = []
for i in range(1, 17):
    imagen_path = f"imagenes/{i}.png"
    imagen = pygame.image.load(imagen_path)
    imagen = pygame.transform.scale(imagen, DIMENCIONES)
    imagenes_preguntas.append(imagen)


# Coordenadas de botones
BOTON_PLAY_X = (310, 550)
BOTON_PLAY_Y = (480, 606)
BOTON_AX = (320, 530)
BOTON_AY = (205, 235)
BOTON_BX = (320, 530)
BOTON_BY = (260, 280)
BOTON_CX = (620, 825)
BOTON_CY = (205, 235)
BOTON_DX = (620, 825)
BOTON_DY = (260, 530)

# Variables
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
x_ventana_izquierda = 0
x_ventana_derecha = ANCHO // 2
indice_pregunta = 0  # Índice de la pregunta actual
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)

# Banderas 
bandera = True
jugar = False
mostrar_botones = True
bandera_jugar = False
tiempo_inicializado = False

def reiniciar_tiempo():
    global tiempo_inicial, tiempo_restante
    tiempo_inicial = pygame.time.get_ticks()  # Reiniciar el tiempo
    tiempo_restante = ultimo_tiempo

while bandera:  # bucle infinito para que se repita la pantalla
    ventana.fill(colores.NEGRO)  # relleno de un color la pantalla
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        print(evento)
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            raton_x, raton_y = evento.pos
            if jugar:
                # Verificar si el clic fue dentro de las coordenadas de los botones de opciones
                if precionar_boton(BOTON_AX, BOTON_AY, "A", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"]):
                    indice_pregunta += 1
                    reiniciar_tiempo()
                elif precionar_boton(BOTON_BX, BOTON_BY, "B", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"]):
                    indice_pregunta += 1
                    reiniciar_tiempo()
                elif precionar_boton(BOTON_CX, BOTON_CY, "C", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"]):
                    indice_pregunta += 1
                    reiniciar_tiempo()
                elif precionar_boton(BOTON_DX, BOTON_DY, "D", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"]):
                    indice_pregunta += 1
                    reiniciar_tiempo()
                
                # Cargar la siguiente pregunta si hay más preguntas
                if indice_pregunta < len(lista_preguntas):
                    pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)
                else:
                    print("¡Has contestado todas las preguntas correctamente!")
                    bandera = False
            else:
                # Verificar si el clic fue dentro de las coordenadas del botón de jugar
                if precionar_boton(BOTON_PLAY_X, BOTON_PLAY_Y, "JUGAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"]):
                    sonido_win = pygame.mixer.Sound(r"sonido\apertura.mp3")
                    sonido_win.set_volume(0.35)
                    sonido_win.play(loops=-1)
                    jugar = True
                    tiempo_inicial = pygame.time.get_ticks()
                    
    ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
    ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))
    if mostrar_botones:
        ventana.blit(fondo_botones, (10, 460))
    if jugar:
        if x_ventana_izquierda > -600:
            x_ventana_izquierda -= VELOCIDAD
            x_ventana_derecha += VELOCIDAD
        elif not tiempo_inicializado:
            tiempo_inicial = pygame.time.get_ticks()  # Inicializar el tiempo cuando las cortinas se han movido completamente
            tiempo_inicializado = True

    if x_ventana_derecha >= ANCHO:
        # Limpiar la pantalla y dibujar el fondo
        ventana.blit(fondo_preguntas, (0, 0))
        # Calcular el tiempo transcurrido y restante
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
        temporizador = fuente_reloj.render(tiempo_restante_str, True, color)

        if jugar:
           ventana.blit(pregunta_actual["pregunta"], (280, 60))
           ventana.blit(pregunta_actual["opcion_a"], (365, 215))
           ventana.blit(pregunta_actual["opcion_b"], (365, 268))
           ventana.blit(pregunta_actual["opcion_c"], (665, 215))
           ventana.blit(pregunta_actual["opcion_d"], (665, 268))
        ventana.blit(temporizador, (237, 637))

    pygame.display.update()  # actualiza la pantalla
    tiempo.tick(FPS)

pygame.quit()  # terminar el proceso de pygame