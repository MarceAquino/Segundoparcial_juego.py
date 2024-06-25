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

# Constantes
tiempo = pygame.time.Clock()
FPS = 30
VELOCIDAD = 3

# Fondo
# Cargar y escalar la imagen de fondo
fondo_cortina_izquierda = pygame.image.load(r"imagenes/fondo_cortina.png")
fondo_cortina_izquierda = pygame.transform.scale(fondo_cortina_izquierda, (ANCHO // 2, ALTO))
fondo_cortina_derecha = pygame.image.load(r"imagenes/fondo_cortina.png")
fondo_cortina_derecha = pygame.transform.scale(fondo_cortina_izquierda, (ANCHO // 2, ALTO))
fondo_cortina_derecha = pygame.transform.flip(fondo_cortina_derecha, True, False)
fondo_botones = pygame.image.load(r"imagenes/fondo_menu.png")
fondo_preguntas = pygame.image.load(r"imagenes\fondo1_preguntas.png")
fondo_preguntas = pygame.transform.scale(fondo_preguntas,(DIMENCIONES))

# Coordenadas de botones
BOTON_PLAY_X = (300, 550)
BOTON_PLAY_Y = (480, 600)
x_ventana_izquierda = 0
x_ventana_derecha = ANCHO // 2

bandera = True
jugar = False
mostrar_botones = True
bandera_jugar = False

while bandera:  # bucle infinito para que se repita la pantalla
    ventana.fill(colores.NEGRO)  # relleno de un color la pantalla
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and bandera_jugar == False:  
                bandera_jugar = True
                raton_x, raton_y = evento.pos
                jugar = precionar_boton(BOTON_PLAY_X, BOTON_PLAY_Y, "JUGAR", raton_x, raton_y)
                if jugar == True :
                    mostrar_botones = False
    
    if jugar == True:
        if x_ventana_izquierda > -ANCHO // 2 and x_ventana_derecha < ANCHO:
            x_ventana_izquierda -= VELOCIDAD
            x_ventana_derecha += VELOCIDAD
    
    ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
    ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))

    if mostrar_botones == True:
        ventana.blit(fondo_botones, (10, 460))
    if mostrar_botones == False and x_ventana_derecha == ANCHO:
        ventana.blit(fondo_preguntas, (0,0))
    pygame.display.update()  # actualiza la pantalla
    tiempo.tick(FPS)

pygame.quit()  # terminar el proceso de pygame