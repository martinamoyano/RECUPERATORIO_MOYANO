def ordenar_posts(lista: list) -> list:
    """
    Ordena la lista de posts por 'user' ascendente.

    Args:
    - lista (list): Lista de diccionarios que contienen los posts.

    Returns:
    - list: Lista ordenada ascendentemente por el campo 'user'.
    """
    # Llamamos a ordenar_lista_campo para ordenar la lista en su lugar.
    ordenar_lista_campo(lista, 'user')
    
    # Devolvemos la lista ya ordenada.
    return lista

def ordenar_lista_campo(lista: list, criterio: str, descendente: bool = False):
    """
    Ordena una lista de diccionarios en función de un campo específico.

    Args:
    - lista (list): Lista de diccionarios a ordenar.
    - criterio (str): El campo por el cual se ordenará la lista.
    - descendente (bool): Indicador de si la ordenación debe ser en orden descendente. Por defecto es `False` (ascendente).

    Returns:
    - None: La función no retorna ningún valor, pero ordena la lista en su lugar.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (not descendente and lista[i][criterio] > lista[j][criterio]) or \
               (descendente and lista[i][criterio] < lista[j][criterio]):
                lista[i], lista[j] = lista[j], lista[i]

# Ejemplo de uso:
posts = [
    {"user": "carlos", "message": "Hola"},
    {"user": "ana", "message": "Buenos días"},
    {"user": "jose", "message": "Buenas tardes"},
]

posts_ordenados = ordenar_posts(posts)
print(posts_ordenados)
