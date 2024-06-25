import pygame

def precionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y: int) -> bool:
   
    mensaje = False 
    sonido_click = pygame.mixer.Sound("sonido\click.wav")
    sonido_click.set_volume(0.35)
    sonido_click.play()
    if coordenadas_x[0] <= raton_x <= coordenadas_x[1] and coordenadas_y[0] <= raton_y <= coordenadas_y[1]: 
        if boton == "JUGAR":
            mensaje = True      
    return mensaje

