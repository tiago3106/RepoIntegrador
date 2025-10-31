#País con mayor y menor población
def mayor_menor_poblacion(paises):
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





