#Función principal de ordenamiento de paises
from manejo_de_archivos import lista_pais
from validaciones import validar_numero
def ordenamiento_principal(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    # Se le pregunta al usuario que opcion
    # de ordenamiento desea
    print(""" 
        1.Ordenar por nombre
        2.Ordenar por población
        3.Ordenar por superficie(ascedente o descendente)""")
    opciones=int(input('Ingrese la opcion deseada: '))
    validar_numero(opciones)
    match opciones:
        case 1:
            #Funcion para ordenar por nombre los paises
            ordenado = False
            while not ordenado:
                ordenado = True
                n = len(paises)
                for i in range(n): #se utiliza el método burbuja para ordenar
                    for j in range(1, n - i - 1):
                        pais_actual = (paises[j][0])
                        pais_siguiente = (paises[j + 1][0])
                        # Si el actual es menor, intercambiamos
                        if pais_actual > pais_siguiente:
                            paises[j], paises[j + 1] = paises[j + 1], paises[j]
                            ordenado = False
            for linea in range(n):
                print(paises[linea]) 
        case 2:
            #Funcion para ordenar la poblacion de mayor a menor
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
            for linea in range(n):
                print(paises[linea])
        case 3:
            decision=validar_numero(input('0.Orden ascedente o 1.Orden descendente: '))
            elecion_3 = [decision - 1] #Se ordenan los paises segun la eleccion del usuario
            if elecion_3 == 0:
                #Funcion para ordenar la superficie ascendente
                n = len(paises)
                ordenado = False
                while not ordenado:
                    ordenado = True
                    for i in range(n): #se utiliza el método burbuja para ordenar
                        for j in range(1, n - i - 1):
                            # Convertimos a entero antes de comparar
                            superficie_actual = int(paises[j][2])
                            superficie_siguiente = int(paises[j + 1][2])
                            # Si el actual es mayor, intercambiamos
                            if superficie_actual > superficie_siguiente:
                                paises[j], paises[j + 1] = paises[j + 1], paises[j] 
                                ordenado = False
                #mostramos en pantalla los paises ordenados
                for linea in paises:
                    print(linea)
            elif elecion_3 == 1:
                #Funcion para ordenar la superficie descendente
                n = len(paises)
                ordenado = False
                while not ordenado:
                    ordenado = True
                    for i in range(n): #se utiliza el método burbuja para ordenar
                        for j in range(1, n - i - 1): 
                            # Convertimos a entero antes de comparar
                            superficie_actual = int(paises[j][2])
                            superficie_siguiente = int(paises[j + 1][2])
                            # Si el actual es mayor, intercambiamos
                            if superficie_actual < superficie_siguiente:
                                paises[j], paises[j + 1] = paises[j + 1], paises[j]
                                ordenado = False
                for linea in paises:
                    print(linea)
            else:
                print('Opcion no valida')