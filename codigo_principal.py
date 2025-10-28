from funcion_menu import menu
from filtrar_pais_2 import filtrar
from manejo_de_archivos import buscar_archivos  
from buscar_pais_1 import buscar_pais
nombre_archivo= buscar_archivos()

bucle = True
while bucle:
    opcion = menu() #llama a la funcion menu que esta en el funcion_menu.py
    match opcion:
        case "1":
            #buscar un país por el nombre
            buscar_pais(nombre_archivo)
        case "2":
            #filtrar paises por continente, rango de poblacion o rango de superficie

            None
        case "3":
            #ordenar paises por nombre, poblacion o superficie(aascedente o descendente)
            None
        case "4":
            #mostrar estadisticas de los paises por pais con mayor o menor poblacion,
            # promedio de poblacion, pais con mayor o menor superficie
            #promediode superficie, cantidad de paises por continente
            None
        case "5":
            #agregar pais
            None
        case "6":   
            #modificar pais
            None
        case "7":
            bucle = False