#Función principal de estadisticas
from manejo_de_archivos import lista_pais
from poblacion_mayor_a_menor import mayor_menor_poblacion
from Promedio_poblacion import promedio_de_la_poblacion
def Estadisticas_generales(nombre_archivo): 
    paises= lista_pais(nombre_archivo)
    print("""
        1.País con mayor y menor población
        2.Promedio de población
        3.Promedio de superficie
        4.Cantidad de países por continente""")
    opcion=int(input('Ingrese la opción deseada: '))
    match opcion:
        case 1:
            mayor_menor_poblacion(paises) #Se muestran los paises con mayor y menor población
        case 2:
            promedio_de_la_poblacion(paises) #Se calcula el promedio de la población de los paises
        case 3:
              None