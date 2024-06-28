import pygame
import constantes

lista_p = []
for i in range(1, 23):
    imagen_path = f"imagenes/{i}.png"
    imagen = pygame.image.load(imagen_path)
    imagen = pygame.transform.scale(imagen, constantes.DIMENCIONES)
    lista_imagenes.append(imagen)
    
   