#Funcion para ordenar la superficie descendente
def superficie_descendente(paises):
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