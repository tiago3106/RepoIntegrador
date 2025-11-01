from funcion_menu import menu
from filtrar_pais_2 import filtrar
from manejo_de_archivos import buscar_archivos, lista_pais 
from buscar_pais_1 import buscar_pais
nombre_archivo= buscar_archivos() 
from validaciones import validar_numero
from Ordenamiento_principal_3 import ordenamiento_principal
from Estadisticas_paises import Estadisticas_generales
paises= lista_pais(nombre_archivo)
bucle = True
while bucle:
    #llama a la funcion menu que esta en el funcion_menu.py
    opcion = validar_numero(menu())
    match opcion:
        case 1:
            # buscar un país por el nombre
            buscar_pais(nombre_archivo)
        case 2:
            # filtrar paises por continente, rango de poblacion o rango de superficie
            filtrar(nombre_archivo)
        case 3:
            # ordenar paises por nombre, poblacion o superficie(aascedente o descendente)
            ordenamiento_principal(nombre_archivo)
        case 4:
            # mostrar estadisticas de los paises por pais con mayor o menor poblacion,
            # promedio de poblacion, pais con mayor o menor superficie
            # promedio de superficie, cantidad de paises por continente
            Estadisticas_generales(nombre_archivo)
        case 5:
            #agregar pais
            None
        case 6:   
            #modificar pais
            None
        case 7:
            bucle = False