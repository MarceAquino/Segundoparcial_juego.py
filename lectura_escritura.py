import json
#----------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_preguntas_csv(path: str) -> list[dict]:
    """
    Carga los datos de las preguntas desde un archivo CSV y los devuelve como una lista de diccionarios.

    Argumentos:
    - path: La ruta del archivo CSV a cargar.

    Retorna:
    - list[dict]: Una lista de diccionarios con la información de las preguntas y respuestas. """
    
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
#----------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_datos_desde_json(path: str) -> tuple[list[str], list[int], list[str]]:
    """
    Carga los datos desde un archivo JSON y los devuelve como tres listas separadas.

    Argumentos:
    - path: La ruta del archivo JSON a cargar.

    Retorna:
    - tuple[list[str], list[int], list[str]]: Una tupla con tres listas: lista de imágenes, lista de premios, lista de sonidos. """
    
    with open(path, "r") as archivo:
        data = json.load(archivo)

    lista_imagenes = data["path"]
    lista_premios = data["premios"]
    lista_sonido = data["sonidos"]

    return lista_imagenes, lista_premios,  lista_sonido
lista_imagenes, lista_premios,  lista_sonido = cargar_datos_desde_json("path_premios.json")
#----------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_premios_csv(path: str) -> list[dict]:
    """
    Carga los datos de premios desde un archivo CSV y los devuelve como una lista de diccionarios.

    Argumentos:
    - path: La ruta del archivo CSV a cargar.

    Retorna:
    - list[dict]: Una lista de diccionarios con la información de los premios. """
    
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
#----------------------------------------------------------------------------------------------------------------------------------------------------   
def guardar_premio_csv(lista_ranking: list[dict], path: str) -> None:
    """
    Guarda la lista de rankings en un archivo CSV.

    Argumentos:
    - lista_ranking: La lista de diccionarios con los rankings a guardar.
    - path: La ruta del archivo CSV donde se guardará la información.
    Retorna:
    - None """
    
    bubble_sort(lista_ranking,"premio")
    with open(path,"w",encoding='utf-8') as archivo:
        archivo.write("ID,premio\n")
        for i in range(5):
            ranking = lista_ranking[i]
            jugador = ranking["ID"]
            premio = ranking["premio"]
         
            archivo.write(f"{jugador},{premio}\n")   
#----------------------------------------------------------------------------------------------------------------------------------------------------
def obtener_maximo(lista_ranking: list[dict], clave: str) -> int | float | bool:
    """
    Obtiene el valor máximo de una clave específica en una lista de diccionarios.

    Argumentos:
    - lista_ranking: La lista de diccionarios donde buscar el valor máximo.
    - clave: La clave sobre la cual buscar el máximo valor.

    Retorna:
    - int | float | bool: El valor máximo encontrado en la lista, puede ser de tipo int, float o bool."""
    
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
#----------------------------------------------------------------------------------------------------------------------------------------------------
def guardar_premio(lista_ranking: list[dict], premio) -> None:
    """
    Guarda un nuevo premio en la lista de rankings.

    Argumentos:
    - lista_ranking: La lista de diccionarios donde se guardará el nuevo premio.
    - premio: El premio a guardar.

    Retorna:
    - None """
    
    jugador = obtener_maximo (lista_ranking, "ID") + 1
    jugador = {
        "ID": jugador,
        "premio": int(premio),    
     }
    
    lista_ranking.append(jugador)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------

               
def bubble_sort(lista_ranking: list[dict], clave: str) -> None:
    """
    Ordena una lista de diccionarios por una clave específica utilizando el algoritmo Bubble Sort.

    Argumentos:
    - lista_ranking: La lista de diccionarios a ordenar.
    - clave: La clave sobre la cual ordenar la lista.
    Retorna:
    - None """
    
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
#----------------------------------------------------------------------------------------------------------------------------------------------------

