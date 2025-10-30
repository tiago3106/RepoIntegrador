def nombre_ordenado(paises):
    ordenado = False
    while not ordenado:
        ordenado = True
        n = len(paises)
        for i in range(n):
            for j in range(1, n - i - 1):
                # Convertimos a entero antes de comparar
                pais_actual = (paises[j][0])
                pais_siguiente = (paises[j + 1][0])
                # Si el actual es menor, intercambiamos
                if pais_actual > pais_siguiente:
                    paises[j], paises[j + 1] = paises[j + 1], paises[j]
                    ordenado = False

    for linea in range(n):
        print(paises[linea], '\n')