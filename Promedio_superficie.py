def promedio_de_la_superficie(paises):
    total_superficie=0
    datos = paises[1:] #para que el for se saltee la linea del encabezado
    cantidad=len(datos)
    for linea in datos:
        total_superficie = total_superficie + int(linea[2]) #Se hace la suma de la superficie de los paises 
    total_superficie= total_superficie/cantidad
    print(f'El promedio de la superficie de los paises es: "{total_superficie}"')