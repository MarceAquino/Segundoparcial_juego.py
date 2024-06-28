import pygame
from lectura_escritura import *
import constantes
imagen = pygame.image.load(lista_imagenes[22])  # Cargar imagen específica
pygame.display.set_icon(imagen)
fondo_cortina_izquierda = pygame.image.load(lista_imagenes[21])
fondo_cortina_izquierda = pygame.transform.scale(fondo_cortina_izquierda, (constantes.ANCHO // 2, constantes.ALTO))
fondo_cortina_derecha = pygame.image.load(lista_imagenes[21])
fondo_cortina_derecha = pygame.transform.scale(fondo_cortina_derecha, (constantes.ANCHO // 2, constantes.ALTO))
fondo_cortina_derecha = pygame.transform.flip(fondo_cortina_derecha, True, False)
fondo_botones = pygame.image.load(lista_imagenes[20])
fondo_preguntas = pygame.image.load(lista_imagenes[16])
fondo_preguntas = pygame.transform.scale(fondo_preguntas, constantes.DIMENCIONES)
fondo_game_over = pygame.image.load(lista_imagenes[17])
fondo_game_over = pygame.transform.scale(fondo_game_over, constantes.DIMENCIONES)
fondo_retiro = pygame.image.load(lista_imagenes[18])
fondo_retiro = pygame.transform.scale(fondo_retiro, constantes.DIMENCIONES)
fondo_ranking = pygame.image.load(lista_imagenes[19])
fondo_ranking = pygame.transform.scale(fondo_ranking, constantes.DIMENCIONES)
