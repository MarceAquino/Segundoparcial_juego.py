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





