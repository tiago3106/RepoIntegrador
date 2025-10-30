def continente_filtrado(paises):
    continente=input("Ingrese el continente a filtrar: ").lower()
    print(f'Los paises que se encuentran en {continente} son:')
    for linea in paises:
        if linea[3] == continente:   
            print(linea)