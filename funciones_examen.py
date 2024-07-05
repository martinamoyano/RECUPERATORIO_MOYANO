from funciones_archivos import *
from funciones_genericas import *
from random import randint
from validaciones import *

# Cargar archivo .CSV
def cargar_archivo()-> list:
    """
    Carga los datos de un archivo CSV y los convierte en una lista de diccionarios.

    Args:
    - None

    Returns:
    - Retorna la lista cargada con los datos del CSV.
    """
    path = input("Por favor ingrese la ruta del archivo .CSV a cargar: ")
    lista_datos = parser_csv(path)
    if lista_datos != None:
        print("¡Archivo cargado con éxito!")
    return lista_datos

# Imprimir lista
def imprimir_lista(lista: list):
    """
    Valida y muestra una lista.

    Args:
    - lista (list): Lista de diccionarios.

    Returns:
    - None
    """
    if validar_lista (lista) == True:
        mostrar_lista(lista)

# Asignar tiempos
def asignar_valores_posts(post)-> dict:
    """
    Asigna valores aleatorios de likes entre 500 y 3000, dislikes con valores entre 300 y 3500 y followers entre 10000 y 20000.

    Args:
    - post (dict): Diccionario que representa un post.

    Returns:
    - dict: El diccionario del post con el valor asignado.
    """
    post['likes'] = randint(500, 3000)
    post['dislikes'] = randint(300, 3500)
    post['followers'] = randint(10000, 20000)
    return post

def asignar_estadisticas(lista:list)-> bool:
    """
    Asigna tiempos a cada bicicleta en la lista utilizando una función de mapeo y muestra los resultados.

    Args:
    - lista (list): Lista de diccionarios que contienen información sobre bicicletas.

    Returns:
    - bool: `True` si los tiempos fueron asignados y cargados correctamente, `False` en caso contrario.

    Raises:
    - TypeError: Si se produce un error durante la asignación de tiempos.
    """
    try:
        lista_datos = map_list(asignar_valores_posts, lista)
        mostrar_lista(lista_datos)
    except TypeError as e:
        print (e)
    if lista_datos:
        datos_cargados = True
    return datos_cargados

# Informar POPULAR
def definir_popular(lista: list) -> dict:
    """
    Define el post más likeado de todos basándose en la mayor cantidad de likes.

    Args:
    - lista (list): Lista de diccionarios que contiene información de posts.

    Returns:
    - dict: Diccionario con el USER del más popular y la cantidad de likes si hay un único ganador,
            o una lista de USERS y la cantidad de likes si hay un empate.
    """
    popular = calcular_maximo_dict(lista, "likes")
    likes_popular = popular["likes"]
    
    users_empatados = []
    for user in lista:
        if user["likes"] == likes_popular:
            users_empatados.append(user["user"])

    if len(users_empatados) == 1:
        return {"Más popular": popular["user"], "Likes": likes_popular}
    return {"Más populares": users_empatados, "Likes": likes_popular}

def informar_popular(lista: list) -> dict:
    """
    Informa el post más popular, mostrando el user o los users empatados en likes.

    Args:
    - lista (list): Lista de diccionarios que contiene información de posts.

    Returns:
    - dict: Diccionario con el post más likeado, indicando el más likeado o los empatados.
    """
    resultado = definir_popular(lista)
    print("------------------------------")
    print("POSTEO MÁS LIKEADO")
    print("------------------------------")
    mostrar_diccionario(resultado)

# Filtrar por likes
def filtrar_por_likes(posts: list) -> list:
    """
    Filtra los posts que tienen 2000 o más likes.

    Args:
    - posts (list): Lista de diccionarios que contienen posts.

    Returns:
    - list: Lista filtrada que contiene solo los posts con 2000 o más likes.
    """
    lista_filtrada = []
    for post in posts:
        if post['likes'] > 2000:
            lista_filtrada.append(post)
    return lista_filtrada

def filtrar_mejores_posts(lista: list):
    """
    Filtra la lista de posts por los que tienen mas de 2000 likes.

    Args:
    - lista (list): Lista de diccionarios que contienen los posts.

    Returns:
    - None: La función no retorna ningún valor, pero genera un archivo CSV si la lista filtrada es válida.

    Prints:
    - Mensajes indicando el éxito de la operación.
    """
    lista_filtrada = filtrar_por_likes(lista)
    if validar_lista(lista_filtrada):
        path = f"mejores_posts.csv"
        generar_csv(path, lista_filtrada)
        print(f"¡Archivo creado con exito en {path}!")

# Filtrar por haters
def filtrar_por_haters(posts: list) -> list:
    """
    Filtra los posts que tienen más dislikes que likes.

    Args:
    - posts (list): Lista de diccionarios que contienen posts.

    Returns:
    - list: Lista filtrada que contiene solo los posts que tienen más dislikes que likes.
    """
    lista_filtrada = []
    for post in posts:
        if post['dislikes'] > post['likes']:
            lista_filtrada.append(post)
    return lista_filtrada
    
def filtrar_haters(lista: list):
    """
    Filtra la lista por los posts que tienen más dislikes que likes.

    Args:
    - lista (list): Lista de diccionarios que contienen los posts.

    Returns:
    - None: La función no retorna ningún valor, pero genera un archivo CSV si la lista filtrada es válida.

    Prints:
    - Mensajes indicando el éxito de la operación.
    """
    lista_filtrada = filtrar_por_haters(lista)
    if validar_lista(lista_filtrada):
        path = f"haters.csv"
        generar_csv(path, lista_filtrada)
        print(f"¡Archivo creado con exito en {path}!")

# Calcular promedio por tipo
def calcular_promedio_followers(lista: list) -> float:
    """
    Calcula y muestra el promedio followers en la lista de posts.

    Args:
    - lista (list): Lista de diccionarios que contiene los posts.

    Returns:
    - promedio: devuelve el promedio de followers de los posts.
    """
    followers = mapear_campo(lista, 'followers')
    promedio = calcular_promedio(followers)
    promedio = int(promedio) #quito las comas

    return promedio

# Ordenar posts ascendente
def ordenar_posts(lista:list)-> bool:
    """
    Ordena la lista de posts por 'user' ascendente.

    Args:
    - lista (list): Lista de diccionarios que contienen los posts.

    Returns:
    - lista_ordenada: Lista ordenada ascendentemente.
    """
    ordenar_lista_campo(lista, 'user')
    
    return lista

# Guardar lista ordenada
def guardar_lista_ordenada(lista: list):
    """
    Guarda la lista ordenada ascendentemente en un archivo JSON llamado 'posts_ordenados.json'.

    Args:
    - lista (list): Lista de diccionarios que contienen los posts.

    Returns:
    - None
    """
    ordenar_posts(lista)
    generar_json("posts_ordenados.json", lista)
    print("Lista ordenada ascendentemente guardada en 'posts_ordenados.json'.")
