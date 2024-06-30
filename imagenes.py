import pygame
from lectura_escritura import *
import constantes
icono = pygame.image.load(lista_imagenes[18])  # Cargar imagen específica
pygame.display.set_icon(icono)
fondo_cortina_izquierda = pygame.image.load(lista_imagenes[16])
fondo_cortina_izquierda = pygame.transform.scale(fondo_cortina_izquierda, (constantes.ANCHO // 2, constantes.ALTO))
fondo_cortina_derecha = pygame.image.load(lista_imagenes[16])
fondo_cortina_derecha = pygame.transform.scale(fondo_cortina_derecha, (constantes.ANCHO // 2, constantes.ALTO))
fondo_cortina_derecha = pygame.transform.flip(fondo_cortina_derecha, True, False)
fondo_botones = pygame.image.load(lista_imagenes[15])
fondo_preguntas = pygame.image.load(lista_imagenes[19])
fondo_preguntas = pygame.transform.scale(fondo_preguntas, constantes.DIMENSIONES)
fondo_game_over = pygame.image.load(lista_imagenes[17])
fondo_game_over = pygame.transform.scale(fondo_game_over, constantes.DIMENSIONES)
fondo_ranking = pygame.image.load(lista_imagenes[20])
fondo_ranking = pygame.transform.scale(fondo_ranking, constantes.DIMENSIONES)
fondo_retiro = pygame.image.load(lista_imagenes[14])
fondo_retiro = pygame.transform.scale(fondo_retiro,constantes.DIMENSIONES)
fondo_ganador = pygame.image.load(lista_imagenes[21])
fondo_ganador = pygame.transform.scale(fondo_ganador,constantes.DIMENSIONES)
fondo_time_over = pygame.image.load(lista_imagenes[22])
fondo_time_over = pygame.transform.scale(fondo_time_over, constantes.DIMENSIONES)

def cargar_imagenes(lista_imagenes):
    imagenes_cargadas = []  
    for i in range(len(lista_imagenes)):
        imagen_cargada = pygame.image.load(lista_imagenes[i])
        imagen_cargada = pygame.transform.scale(imagen_cargada,constantes.DIMENSIONES)
        imagenes_cargadas.append(imagen_cargada)
    return imagenes_cargadas