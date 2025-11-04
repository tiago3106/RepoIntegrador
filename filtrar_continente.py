def continente_filtrado(paises):
    continente=input("Ingrese el continente a filtrar: ").lower()
    print(f'Los paises que se encuentran en {continente} son:')
    for linea in paises: #filtra por continente si tiene la linea mas de 3 elementos y el elemento 3 es igual al continente ingresado
        if len(linea) > 3 and linea[3] == continente:   
            print(linea)