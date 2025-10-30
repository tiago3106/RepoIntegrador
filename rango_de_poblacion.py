from validaciones import validar_numero
def rango_de_poblacion(paises):
    bandera = False
    minimo,maximo = maximo_minimo_datos(paises)
    print(f"El maximo posible es {maximo}")
    print(f"El minimo posible es {minimo} ")
    rango_minimo = input("Ingrese el rango minimo de poblacion de los paises buscados: ").strip()
    rango_maximo = input("Ingrese el rango maximo de poblacion de los paises buscados").strip()
    print(f'Los paises que se encuentran entre {rango_minimo} y {rango_maximo} son:')
    for linea in (1,len(paises)):
        if linea > 2 and linea[2] >= rango_minimo and linea[2] <= rango_maximo:   
            print(linea)
            bandera = True
    if bandera == False:
        print(f"No hay ningun pais con un rando de pobalcion entre {rango_minimo} y {rango_maximo}")

def maximo_minimo_datos(paises):
    n = len(paises)
    maximo = int(0)
    minimo = int(0)
    for linea in range(1, n):
        if linea > 2 and linea[2] >= maximo:
            maximo = linea[2]
        if linea > 3 and linea[2] <= minimo:
            minimo = linea[2]
    return minimo,maximo
