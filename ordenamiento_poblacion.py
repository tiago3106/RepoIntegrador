def poblacion_ordenada(paises):
    ordenado = False
    while not ordenado:
        ordenado = True
        n = len(paises)
        for i in range(n):
            for j in range(1, n - i - 1):
                # Convertimos a entero antes de comparar
                poblacion_actual = int(paises[j][1])
                poblacion_siguiente = int(paises[j + 1][1])
                # Si el actual es menor, intercambiamos
                if poblacion_actual < poblacion_siguiente:
                    paises[j], paises[j + 1] = paises[j + 1], paises[j]
                    ordenado = False

    for linea in range(n):
        print(paises[linea], '\n')