#------------------------------------------------------------------------------
def cargar_peliculas_csv(path: str) -> list[dict]:
    """
    Carga los datos de las películas desde un archivo CSV y los devuelve como una lista de diccionarios.

    parametro path: La ruta del archivo CSV a cargar.
    return: Una lista de diccionarios con la información de las películas.
    """
    lista_preguntas = []
    

    with open(path,"r",encoding='utf-8') as archivo:
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

lista_preguntas = cargar_peliculas_csv("Segundoparcial_juego.py\Preguntas.csv")

print(lista_preguntas)