from validaciones import validar_numero
def Estadisticas_generales(paises): 
    
    print("""
        1.País con mayor y menor población
        2.Promedio de población
        3.Promedio de superficie
        4.Cantidad de países por continente""")
    opcion = validar_numero(input('Ingrese la opción deseada: '))

    # Validamos si la lista tiene datos antes de calcular
    if not paises and opcion != 4: # Si la lista está vacía
        print("No hay países en la lista para calcular estadísticas.")
        return
    match opcion:
        case 1:
            pais_mayor_pob = max(paises, key=lambda item: item['poblacion'])
            pais_menor_pob = min(paises, key=lambda item: item['poblacion'])
            print(f"País con mayor población: {pais_mayor_pob['pais']} ({pais_mayor_pob['poblacion']})\n")
            print(f"País con menor población: {pais_menor_pob['pais']} ({pais_menor_pob['poblacion']})")
        case 2:
            total_poblacion = 0
            for pais in paises:
                total_poblacion += pais['poblacion'] 
            # Dividimos por la longitud total de 'paises'
            promedio = total_poblacion / len(paises)
            print(f'El promedio de la población de los paises es: {promedio:.2f}') # .2f redondea a 2 decimales
        case 3:
            total_superficie = 0
            for pais in paises:
                total_superficie += pais['superficie']
            promedio_sup = total_superficie / len(paises)
            print(f'El promedio de la superficie de los paises es: {promedio_sup:.2f}')
        case 4:
            print("--- Cantidad de Países por Continente ---")
            conteo_continentes = {}
            for pais in paises:
                # Obtiene el continente (ej. "Asia", "Europa")
                continente = pais['continente'] 
                # Incrementa el contador en el diccionario
                conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
            if conteo_continentes:
                for continente, cantidad in conteo_continentes.items():
                    print(f'{continente}: {cantidad} países')
            else:
                print("No hay países en la lista.")
            # --- FIN DE LA LÓGICA OPTIMIZADA --- 
        case _:
            print('Opción inválida')