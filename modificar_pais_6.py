from validaciones import pedir_nombre, validar_numero

def modificar_pais(paises):
    nombre_buscado = pedir_nombre(" pais a modificar").strip().title()
    encontrado = False
    for pais in paises: # 'pais' es un diccionario
        if pais['pais'] == nombre_buscado:
            print(f"País encontrado. Datos actuales: {pais}")
            #Pedir los nuevos datos
            nuevo_continente = pedir_nombre(" nuevo continente").title()
            nueva_superficie = validar_numero(input(f"Ingrese nueva superficie (actual: {pais['superficie']}): "))
            if nueva_superficie is None:
                print("Superficie no válida. Modificación cancelada.")
                return # Salir de la función
            nueva_poblacion = validar_numero(input(f"Ingrese nueva población (actual: {pais['poblacion']}): "))
            if nueva_poblacion is None:
                print("Población no válida. Modificación cancelada.")
                return # Salir de la función
            pais['continente'] = nuevo_continente
            pais['superficie'] = nueva_superficie
            pais['poblacion'] = nueva_poblacion
            encontrado = True
            print(f"País '{nombre_buscado}' actualizado en la sesión.")
            print("(Recuerda guardar [Opción 7] para aplicar al archivo).")
            break # Salir del bucle 'for' porque ya encontramos el país

    if not encontrado:
        print(f"El país '{nombre_buscado}' no se encuentra en la lista.")