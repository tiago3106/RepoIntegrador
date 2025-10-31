def promedio_de_la_poblacion(paises):
    total_poblacion=0
    datos = paises[1:] #para que el for se saltee la linea del encabezado
    cantidad=len(datos)
    for linea in datos:
        total_poblacion = total_poblacion + int(linea[1]) #Se hace la suma de todas las poblaciones
    total_poblacion= total_poblacion/cantidad
    print(f'El promedio de la población de los paises es: "{total_poblacion}"')