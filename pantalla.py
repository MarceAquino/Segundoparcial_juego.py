import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *

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

# Coordenadas de botones
BOTON_PLAY_X = (300, 550)
BOTON_PLAY_Y = (480, 600)
x_ventana_izquierda = 0
x_ventana_derecha = ANCHO // 2

# Banderas 
bandera = True
jugar = False
mostrar_botones = True
bandera_jugar = False
tiempo_inicializado = False

while bandera == True:  # bucle infinito para que se repita la pantalla
    ventana.fill(colores.NEGRO)  # relleno de un color la pantalla
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        print(evento)
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and bandera_jugar == False:  
                raton_x, raton_y = evento.pos
                jugar = precionar_boton(BOTON_PLAY_X, BOTON_PLAY_Y, "JUGAR", raton_x, raton_y)
            if jugar == True:
                bandera_jugar = True
                mostrar_botones = False
                tiempo_inicializado = False  # Asegúrate de reiniciar la bandera del tiempo inicial

    if jugar == True:
        if x_ventana_izquierda > -ANCHO // 2 and x_ventana_derecha < ANCHO:
            x_ventana_izquierda -= VELOCIDAD
            x_ventana_derecha += VELOCIDAD
        elif tiempo_inicializado == False:
            tiempo_inicial = pygame.time.get_ticks()  # Inicializar el tiempo cuando las cortinas se han movido completamente
            tiempo_inicializado = True

    ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
    ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))

    if mostrar_botones == True:
        ventana.blit(fondo_botones, (10, 460))
    if mostrar_botones == False and x_ventana_derecha >= ANCHO:
        # Limpiar la pantalla y dibujar el fondo
        ventana.blit(fondo_preguntas, (0, 0))
        
        # Calcular el tiempo transcurrido y restante
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        tiempo_restante = ultimo_tiempo - int(tiempo_transcurrido / 1000)
        if tiempo_restante < 0:
            tiempo_restante = 0
        
        # Dibujar el tiempo restante en la pantalla
        if tiempo_restante > 20:
            temporizador = fuente_reloj.render(f"{tiempo_restante}", True, colores.NEGRO)
        elif tiempo_restante > 10:
            temporizador = fuente_reloj.render(f"{tiempo_restante}", True, colores.AMARILLO)
        else:
            temporizador = fuente_reloj.render(f"{tiempo_restante}", True, colores.ROJO)
        ventana.blit(temporizador, (240, 640))
    
    pygame.display.update()  # actualiza la pantalla
    tiempo.tick(FPS)

pygame.quit()  # terminar el proceso de pygame
