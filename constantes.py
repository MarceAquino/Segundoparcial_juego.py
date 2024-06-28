ANCHO = 1200
ALTO = 800
DIMENCIONES = (ANCHO, ALTO)
FPS = 30
VELOCIDAD = 3
ULTIMO_TIEMPO = 30
BOTON_PLAY_X = (310, 550)
BOTON_PLAY_Y = (480, 606)
BOTON_AX = (320, 530)
BOTON_AY = (205, 235)
BOTON_BX = (320, 530)
BOTON_BY = (260, 280)
BOTON_CX = (620, 825)
BOTON_CY = (205, 235)
BOTON_DX = (620, 825)
BOTON_DY = (260, 280)
BOTON_CONTINUARX = (1050,1170)
BOTON_CONTINUARY = (620,740)
BOTON_RETIROX = (1050,1170)
BOTON_RETIROY = (430,550)
BOTON_RANKINX = (300,555)
BOTON_RANKINY = (640,763)
BOTON_REINICIARX = (1020,1110)
BOTON_REINICIARY = (14,80)
RECORDX = (800,925) 
RECORDY = (238,343)
REINICIO_FINX = (970,1100) 
REINICIO_FINY = (238,343)
# def mostrar_todas_peliculas(lista: list[dict]):
#     """
#     Crea una matriz a la cual agrega todos los diccionarios de la lista
#     y luego recorre la matriz dandole formato de tabla para mostrarla.
#     Argumentos:
    
# lista[dict] Una lista de diccionarios. 
#   Retorna:
  
# None: Esta función no devuelve nada."""
# matriz_datos_peliculas = []
# fila = ["Titulo","Género","Año de lanzamiento","Duración","ATP","Plataformas"]
# matriz_datos_peliculas.append(fila)

#   for pelicula in lista:
#       titulo = pelicula['titulo']
#       genero = pelicula['genero']
#       anio = str(pelicula['anio'])
#       duracion = str(pelicula['duracion'])
#       atp = pelicula["ATP"]
#       plataformas = '-'.join(pelicula['plataformas'])

#       matriz_datos_peliculas.append([titulo, genero, anio, duracion, atp, plataformas])


#     ancho_columnas = [50, 20, 20, 15, 6, 70]
 
#     ancho_maximo = 200

#     print("" ancho_maximo)
#     fila_formateada = ''
#     for i in range(len(matriz_datos_peliculas[0])):
#         columna = matriz_datos_peliculas[0][i]
#         ancho = ancho_columnas[i]
#         texto = centrar_texto(columna, ancho)
#         fila_formateada += f"| {texto} "
#     print(fila_formateada + '|')
#     print("-" * ancho_maximo)

#     for i in range(1, len(matriz_datos_peliculas)):
#         fila_formateada = ''
#         for j in range(len(matriz_datos_peliculas[i])):
#             columna = matriz_datos_peliculas[i][j]
#             ancho = ancho_columnas[j]
#             texto = centrar_texto(columna, ancho)
#             fila_formateada += f"| {texto} "
#         print(fila_formateada + '|')

#     print("" ancho_maximo)
