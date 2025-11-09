from validaciones import validar_numero

def ordenamiento_principal(paises):
    """
    Ordena la lista de países usando el método .sort()
    """
    print(""" 
        1.Ordenar por nombre (A-Z)
        2.Ordenar por población (Mayor a Menor)
        3.Ordenar por superficie""")
    
    opciones = validar_numero(input('Ingrese la opcion deseada: '))

    match opciones:
        case 1:
            # Ordena la lista 'paises' usando la clave 'pais'
            paises.sort(key=lambda item: item['pais'])
            print("--- Países ordenados por nombre (A-Z) ---")
            
        case 2:
            # Ordena por 'poblacion', en orden reverso
            paises.sort(key=lambda item: item['poblacion'], reverse=True)
            print("--- Países ordenados por población (Mayor a Menor) ---")

        case 3:
            decision = validar_numero(input('0. Orden ascendente o 1. Orden descendente: '))
            if decision == 0:
                # Ordena por 'superficie', ascendente
                paises.sort(key=lambda item: item['superficie'])
                print("--- Países ordenados por superficie (Ascendente) ---")
            elif decision == 1:
                # Ordena por 'superficie', descendente
                paises.sort(key=lambda item: item['superficie'], reverse=True)
                print("--- Países ordenados por superficie (Descendente) ---")
            else:
                print('Opcion no valida')
        case _:
            print("Opción no válida.")
            return # Salir si la opción no es válida

    # Imprimir la lista ordenada (solo se ejecuta si la opción fue válida)
    for pais in paises:
        # Imprime los datos de forma más legible
        print(f"- País: {pais['pais']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']}")