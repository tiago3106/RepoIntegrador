#Función principal de estadisticas
from manejo_de_archivos import lista_pais
from pais_por_continente import cant_pais_por_continente
from validaciones import validar_numero
def Estadisticas_generales(nombre_archivo): 
    paises= lista_pais(nombre_archivo)
    print("""
        1.País con mayor y menor población
        2.Promedio de población
        3.Promedio de superficie
        4.Cantidad de países por continente""")
    opcion=validar_numero(input('Ingrese la opción deseada: '))
    match opcion:
        case 1:
            #País con mayor y menor población
            ordenado = False
            while not ordenado:
                ordenado = True
                n = len(paises)
                for i in range(n): #se utiliza el método burbuja para ordenar
                    for j in range(1, n - i - 1):
                        # Convertimos a entero antes de comparar
                        poblacion_actual = int(paises[j][1])
                        poblacion_siguiente = int(paises[j + 1][1])
                        # Si el actual es menor, intercambiamos
                        if poblacion_actual < poblacion_siguiente:
                            paises[j], paises[j + 1] = paises[j + 1], paises[j]
                            ordenado = False

            for linea in range(1):
                print(f'El pais con mayor pobacion es: "{paises[1]}"')
                print(f'El pais con menor pobacion es: "{paises[-1]}"')
        case 2:
            total_poblacion=0
            datos = paises[1:] #para que el for se saltee la linea del encabezado
            cantidad=len(datos)
            for linea in datos:
                total_poblacion = total_poblacion + int(linea[1]) #Se hace la suma de todas las poblaciones
            total_poblacion= total_poblacion/cantidad #Se calcula el promedio
            print(f'El promedio de la población de los paises es: "{total_poblacion}"')
        case 3:
            total_superficie=0
            datos = paises[1:] #para que el for se saltee la linea del encabezado
            cantidad=len(datos)
            for linea in datos:
                total_superficie = total_superficie + int(linea[2]) #Se hace la suma de la superficie de los paises 
            total_superficie= total_superficie/cantidad
            print(f'El promedio de la superficie de los paises es: "{total_superficie}"')
        case 4:
            #este si lo hicimos en funcion a parte por que es muy largo
            cant_pais_por_continente(paises) #Se buscan paises por continentes
        case _:
            print('Opción inválida')