import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *
pygame.init()
import pygame
import colores
from sonido import *
from imagenes import *
from funciones import *
from lectura_escritura import *
import constantes

pygame.init()
ventana = pygame.display.set_mode(constantes.DIMENCIONES)
pygame.display.set_caption("¿Quién quiere ser millonario?")
fuente_reloj = pygame.font.SysFont('arialblack', 60)

# cargar pregunta
imagenes_preguntas = []
for i in range(1, 17):
    imagen_path = f"imagenes/{i}.png"
    imagen = pygame.image.load(imagen_path)
    imagen = pygame.transform.scale(imagen, constantes.DIMENCIONES)
    imagenes_preguntas.append(imagen)
    
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
indice_pregunta = 0  # Índice de la pregunta actual
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta) # cargar la primer pregunta
x_ventana_izquierda = 0
x_ventana_derecha = constantes.ANCHO // 2
# Banderas 
bandera = True
jugar = False
ranking = False
mostrar_botones = True
bandera_jugar = False
tiempo_inicializado = False
game_over = False
resultado_opcion = "correcta"
retirarse = False

# Inicializar el tiempo y el reloj
tiempo_inicial, tiempo_restante = reiniciar_tiempo(constantes.ULTIMO_TIEMPO)
tiempo = pygame.time.Clock()

while bandera == True:  # bucle infinito para que se repita la pantalla
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            raton_x, raton_y = evento.pos
            
            if jugar == "JUGAR" and game_over == False and retirarse == False:
                opciones = ["A", "B", "C", "D"]
                coordenadas_botones = {
                    "A": (constantes.BOTON_AX, constantes.BOTON_AY),
                    "B": (constantes.BOTON_BX, constantes.BOTON_BY),
                    "C": (constantes.BOTON_CX, constantes.BOTON_CY),
                    "D": (constantes.BOTON_DX, constantes.BOTON_DY)
                }
                
                alguna_correcta = False