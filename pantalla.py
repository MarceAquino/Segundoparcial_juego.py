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
ULTIMO_TIEMPO = 30

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
fondo_game_over = pygame.image.load(r"imagenes\game_over.jpeg")
fondo_game_over = pygame.transform.scale(fondo_game_over,DIMENCIONES)

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
BOTON_DY = (260, 280)
BOTON_CONTINUARX = (1050,1170)
BOTON_CONTINUARY = (620,740)
BOTON_RETIRO = (1050,1170)
BOTON_RETIRO = (430,550)

# Variables
lista_preguntas = cargar_preguntas_csv("Preguntas.csv")
x_ventana_izquierda = 0
x_ventana_derecha = ANCHO // 2
indice_pregunta = 0  # Índice de la pregunta actual
pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta) # cargar la primer pregunta

# Banderas 
bandera = True
jugar = False
mostrar_botones = True
bandera_jugar = False
tiempo_inicializado = False
game_over = False
pregunta = "correcta"


# Inicializar el tiempo y el reloj
tiempo_inicial, tiempo_restante = reiniciar_tiempo(0, ULTIMO_TIEMPO)
tiempo = pygame.time.Clock()

while bandera == True:  # bucle infinito para que se repita la pantalla
   
    ventana.fill(colores.NEGRO)  # relleno de un color la pantalla
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        print(evento)
        if evento.type == pygame.QUIT:  # pregunto si se presionó la X de la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
            raton_x, raton_y = evento.pos
            
            if jugar == "JUGAR" and game_over == False:
                opciones = ["A", "B", "C", "D"]
                coordenadas_botones = {
                    "A": (BOTON_AX, BOTON_AY),
                    "B": (BOTON_BX, BOTON_BY),
                    "C": (BOTON_CX, BOTON_CY),
                    "D": (BOTON_DX, BOTON_DY)
                }
                
                alguna_correcta = False
                
                for opcion in opciones:
                    coordenadas_x, coordenadas_y = coordenadas_botones[opcion]
                    resultado = presionar_boton(coordenadas_x, coordenadas_y, opcion, raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                    
                    if resultado == "CORRECTA":
                        indice_pregunta += 1
                        tiempo_inicial, tiempo_restante = reiniciar_tiempo(tiempo_inicial, ULTIMO_TIEMPO)
                        alguna_correcta = True
                        pregunta = "siguiente"
                        break
                    elif resultado == "INCORRECTA":
                        pregunta = "incorrecta"
                       
                
                if alguna_correcta and indice_pregunta < len(lista_preguntas):
                    pregunta_actual = obtener_preguntas_opciones(lista_preguntas, indice_pregunta)   
                         
            else:
                jugar = presionar_boton(BOTON_PLAY_X, BOTON_PLAY_Y, "JUGAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                tiempo_inicial, tiempo_restante = reiniciar_tiempo(tiempo_inicial, ULTIMO_TIEMPO)    
                                        

    
    #cortinas y botones bart
    ventana.blit(fondo_cortina_izquierda, (x_ventana_izquierda, 0))
    ventana.blit(fondo_cortina_derecha, (x_ventana_derecha, 0))
    if mostrar_botones == True:
        ventana.blit(fondo_botones, (10, 460))
    if jugar == "JUGAR":
        if x_ventana_izquierda > -600:
            x_ventana_izquierda -= VELOCIDAD
            x_ventana_derecha += VELOCIDAD
        elif tiempo_inicializado == False:
            tiempo_inicial = pygame.time.get_ticks()  # Inicializar el tiempo cuando las cortinas se han movido completamente
            tiempo_inicializado = True

    if x_ventana_derecha >= ANCHO :
        # Limpiar la pantalla y dibujar el fondo
        if pregunta == "incorrecta" or tiempo_restante == 0:
            game_over = True
            ventana.blit(fondo_game_over,(0,0))
            
        else: 
            if pregunta == "siguiente":  
                ventana.blit((imagenes_preguntas[indice_pregunta]),(0,0)) 
                continuar = presionar_boton(BOTON_CONTINUARX,BOTON_CONTINUARY, "CONTINUAR", raton_x, raton_y, pregunta_actual["opcion_correcta"], pregunta_actual["opciones"])
                if continuar == "CONTINUAR":
                    pregunta = "correcta"
                    
            else:  
                ventana.blit(fondo_preguntas, (0, 0))
                ventana.blit(pregunta_actual["pregunta"], (280, 60))
                ventana.blit(pregunta_actual["opcion_a"], (365, 210))
                ventana.blit(pregunta_actual["opcion_b"], (365, 265))
                ventana.blit(pregunta_actual["opcion_c"], (665, 210))
                ventana.blit(pregunta_actual["opcion_d"], (665, 265))
                
                # Calcular el tiempo transcurrido y restante
                tiempo_actual = pygame.time.get_ticks()
                tiempo_transcurrido = tiempo_actual - tiempo_inicial
                tiempo_restante = ULTIMO_TIEMPO - int(tiempo_transcurrido / 1000)
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
                ventana.blit(temporizador, (237, 637))
      
                
            
    pygame.display.update()  # actualiza la pantalla
