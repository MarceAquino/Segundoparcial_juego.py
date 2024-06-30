import json
import pygame
import constantes


def cargar_preguntas_csv(path: str) -> list[dict]:
    """
    Carga los datos de las preguntas desde un archivo CSV y los devuelve como una lista de diccionarios.

    parametro path: La ruta del archivo CSV a cargar.
    return: Una lista de diccionarios con la información de las preguntas y respuestas.
    """
    lista_preguntas = []
    
    with open(path, "r", encoding='utf-8') as archivo:
        lineas = archivo.readlines()

        for linea in lineas[1:]:  
            datos = linea.split(",")
            pregunta = datos[0]
            opcion_a = datos[1]
            opcion_b = datos[2]
            opcion_c = datos[3]
            opcion_d = datos[4]
            opcion_correcta = datos[5]
            
            cuestionario = {
                "pregunta": pregunta,
                "opcion_a": opcion_a,
                "opcion_b": opcion_b,
                "opcion_c": opcion_c,
                "opcion_d": opcion_d,
                "opcion_correcta": opcion_correcta.replace("\n", "")
            }

            lista_preguntas.append(cuestionario)

    return lista_preguntas


def cargar_datos_desde_json(path):
    with open(path, "r") as archivo:
        data = json.load(archivo)

    lista_imagenes = data["path"]
    lista_premios = data["premios"]
    lista_sonido = data["sonidos"]

    return lista_imagenes, lista_premios,  lista_sonido
lista_imagenes, lista_premios,  lista_sonido = cargar_datos_desde_json("path_premios.json")

def cargar_premios_csv(path: str) -> list[dict]:
 
    lista_ranking = []
    
    with open(path, "r", encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            if linea.strip():  # Check if the line is not empty
                datos = linea.strip().split(",")
                if len(datos) == 2:
                    jugador = int(datos[0])
                    premio = int(datos[1].replace("\n", ""))
                    
                    ranking = {
                        "ID": jugador,
                        "premio": premio
                    }
                    lista_ranking.append(ranking)
               
    
    return lista_ranking[:5]

def obtener_maximo (lista_ranking: list, clave: str) -> int | float | bool:
    
    base = None
    bandera = True
    mensaje = False
    for ranking in lista_ranking:
        dato = ranking.get(clave)
        if bandera == True or dato > base:
            base = dato
            mensaje = base
            bandera = False
       
    return mensaje

def guardar_premio (lista_ranking: list[dict],premio) -> dict:
    
    jugador = obtener_maximo (lista_ranking, "ID") + 1
    jugador = {
        "ID": jugador,
        "premio": int(premio),    
     }
    lista_ranking.append(jugador)


    
def guardar_premio_csv(lista_ranking: list[dict], path: str):
    
    bubble_sort(lista_ranking,"premio")
    with open(path,"w",encoding='utf-8') as archivo:
        archivo.write("ID,premio\n")
        for i in range(5):
            ranking = lista_ranking[i]
            jugador = ranking["ID"]
            premio = ranking["premio"]
         

            archivo.write(f"{jugador},{premio}\n")   
               
def bubble_sort(lista_ranking: list[dict], clave: str) -> None:
  
    for i in range(len(lista_ranking)):
        intercambio = False
        for j in range(len(lista_ranking) - 1 - i):
            if lista_ranking[j][clave] < lista_ranking[j + 1][clave]:
                auxiliar = lista_ranking[j]
                lista_ranking[j] = lista_ranking[j + 1]
                lista_ranking[j + 1] = auxiliar
                intercambio = True
           
        if intercambio != True:
            break


