
def precionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y: int) -> bool:
    mensaje = False
    if coordenadas_x[0] <= raton_x <= coordenadas_x[1] and coordenadas_y[0] <= raton_y <= coordenadas_y[1]:
        print(f"Tocaste el boton: {boton}")
        if boton == "JUGAR":
            mensaje = True
            
    return mensaje

