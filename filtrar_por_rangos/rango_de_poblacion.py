from validaciones import validar_numero

def rango_de_poblacion(paises):
    """Filtra países por rango de población. (Versión simplificada)"""
    
    # --- Encontrar Min/Max ---
    minimo_en_lista_dict = min(paises, key=lambda item: item["poblacion"])
    maximo_en_lista_dict = max(paises, key=lambda item: item["poblacion"])

    minimo_en_lista_valor = minimo_en_lista_dict["poblacion"] 
    maximo_en_lista_valor = maximo_en_lista_dict["poblacion"] 
    
    print(f"La población mínima en la lista es: {minimo_en_lista_valor}")
    print(f"La población máxima en la lista es: {maximo_en_lista_valor}")

    # --- Pedir y validar rango mínimo ---
    while True:
        entrada_min = validar_numero(input("Ingrese el rango mínimo de población: ").strip())
        if entrada_min is not None:
            rango_min = entrada_min
            if rango_min >= minimo_en_lista_valor:
                break
            else:
                print(f"Valor menor al mínimo: {minimo_en_lista_valor}. Intente nuevamente.")
    
    # --- Pedir y validar rango máximo ---
    while True:
        entrada_max = validar_numero(input("Ingrese el rango máximo de población: ").strip())
        if entrada_max is not None:
            rango_max = entrada_max
            if rango_max <= maximo_en_lista_valor:
                break
            else:
                print(f"Valor excede el máximo: {maximo_en_lista_valor}. Intente nuevamente.")
    
    print(f'Los países que se encuentran entre {rango_min} y {rango_max} son:')

    # --- Bucle de filtrado  ---
    encontrados = []
    
    for pais in paises: 
        pobl = pais["poblacion"] # pobl es poblacion
        
        if rango_min <= pobl <= rango_max:
            encontrados.append((pais["pais"], pobl, pais["continente"]))
    #mostrar en pantalla.
    if encontrados:
        for pais in encontrados:
            print(f"País: {pais[0]}, Población: {pais[1]}, Continente: {pais[2]}")
    else:
        print(f"No hay ningún país con un rango de población entre {rango_min} y {rango_max}")