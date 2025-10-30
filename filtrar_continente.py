def continente_filtrado(paises):
    continente=input("Ingrese el continente a filtrar: ").lower()
    print(f'Los paises que se encuentran en {continente} son:')
    for linea in paises:
        if len(linea) > 3 and linea[3] == continente:   
            print(linea)