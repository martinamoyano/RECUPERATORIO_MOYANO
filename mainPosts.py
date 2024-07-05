from funciones_archivos import *
from funciones_genericas import *
from funciones_examen import *
from validaciones import *

menu = (
    '''¡BIENVENIDO AL MENU!
    1. Cargar archivo .CSV
    2. Imprimir lista de posts
    3. Asignar estadísticas
    4. Filtrar por mejores posts
    5. Filtrar por haters
    6. Informar promedio de followers
    7. Ordenar los datos por nombre de USER ascendente
    8. Mostrar más popular
    9. Salir
    '''
)

def iniciar_programa(menu):
    """
    Función principal que gestiona el menú de los posts de una red social.

    Args:
    - menu (str): Cadena de texto que muestra el menú de opciones al usuario.

    Variables internas:
    - lista_datos (list): Lista que almacena los datos cargados desde el archivo CSV.
    - lista_opciones (list): Lista de cadenas que representan las opciones válidas del menú.
    - estadisticas (bool): Indicador de si los valores han sido asignados a los posts.
    - seguir (bool): Controla el bucle principal para continuar o finalizar el programa.

    Operaciones:
    1. Muestra el menú de opciones al usuario.
    2. Solicita la selección de una opción del menú.
    3. Limpia la pantalla.
    4. Valida la opción seleccionada contra las opciones disponibles.
    5. Realiza la acción correspondiente basada en la opción seleccionada.
    6. Solicita confirmación para salir del programa.
    7. Evalúa la continuación del bucle principal o la finalización del programa.

    Returns:
    - None: La función no retorna ningún valor, controla la interacción con el usuario.
    """
    lista_datos = []
    lista_opciones = ["1", "2","3","4","5","6","7","8","9"]
    carga = False
    estadisticas = False
    seguir = True

    while seguir:
        print(menu)
        opcion = input("Elija una opción (1-9): ")

        system("cls")
        if buscar_en_lista(lista_opciones, opcion) == False:
            print("OPCIÓN NO VÁLIDA. Intente nuevamente (1-9) ")
            pausa()
            limpiar_pantalla()
        else:   
            if opcion != "1" and opcion != "9" and len(lista_datos) == 0:
                print("Debe cargar un archivo CSV primero. (Opción 1)")
            else:
                match opcion:
                    case "1":
                        try:
                            if carga == False:
                                lista_datos = cargar_archivo()
                                carga = True
                            else:
                                print("¡El archivo .CSV ya fue cargado!")
                        except FileNotFoundError as e:
                            print(e)
                    case "2":
                        imprimir_lista(lista_datos)
                    case "3":
                        estadisticas = asignar_estadisticas(lista_datos)
                    case "4":
                        if estadisticas:
                            filtrar_mejores_posts(lista_datos)
                        else:
                            print("Para filtrar por mejores posts, primero se deben asignar los valores. (Opción 3)")
                    case "5":
                        if estadisticas:
                            filtrar_haters(lista_datos)
                        else:
                            print("Para filtrar por haters, primero se deben asignar los valores. (Opción 3)")
                        pass
                    case "6":
                        if estadisticas:
                            promedio = calcular_promedio_followers(lista_datos)
                            print(f"El promedio de followers es: {promedio}")
                        else:
                            print("Para calcular el promedio de followers primero se deben asignar. (Opción 3)")
                    case "7":
                        if estadisticas:
                            guardar_lista_ordenada(lista_datos)
                        else:
                            print("Para ordenar los datos por nombre de USER ascendente, primero debe asignar los valores. (Opción 3)")
                    case "8":
                        if estadisticas:
                            informar_popular(lista_datos)
                        else:
                            print("Para mostrar el nombre del user o users con el posteo más likeado, primero se deben asignar los valores. (Opción 3)")
                    case "9":
                        respuesta = input("¿Seguro desea salir? (si/no): ").lower()
                        if respuesta == "si":
                            seguir = False
                        elif respuesta != "no":
                            print("RESPUESTA NO VÁLIDA. Intente nuevamente")
                    case _:
                        print("OPCIÓN NO VÁLIDA, intente nuevamente (1-9)")

            if seguir:
                input("Presione Enter para continuar...")
                limpiar_pantalla()

        print("¡Gracias por utilizar nuestro programa!")

iniciar_programa(menu)

