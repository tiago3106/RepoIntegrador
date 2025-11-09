from validaciones import validar_numero

def rango_de_superficie(paises):
    """Filtra países por rango de superficie (datos limpios)."""
    
    # --- Encontrar Min/Max ---
    minimo_en_lista_dict = min(paises, key=lambda item: item["superficie"])
    maximo_en_lista_dict = max(paises, key=lambda item: item["superficie"])

    # Extrae el numero nomas
    minimo_en_lista_valor = minimo_en_lista_dict["superficie"]
    maximo_en_lista_valor = maximo_en_lista_dict["superficie"]
    
    print(f"La superficie mínima en la lista es: {minimo_en_lista_valor}")
    print(f"La superficie máxima en la lista es: {maximo_en_lista_valor}")

    # --- Pedir y validar rango mínimo ---
    while True:
        entrada_min = validar_numero(input("Ingrese el rango mínimo de superficie: ").strip())
        if entrada_min is not None:
            rango_min = entrada_min
            if rango_min >= minimo_en_lista_valor:
                break
            else:
                print(f"Valor menor al mínimo: {minimo_en_lista_valor}. Intente nuevamente.")
    
    # --- Pedir y validar rango máximo ---
    while True:
        entrada_max = validar_numero(input("Ingrese el rango máximo de superficie: ").strip())
        if entrada_max is not None:
            rango_max = entrada_max
            if rango_max <= maximo_en_lista_valor:
                break
            else:
                print(f"Valor excede el máximo: {maximo_en_lista_valor}. Intente nuevamente.")
    print(f'Los países que se encuentran entre {rango_min} y {rango_max} son:')
    # --- Bucle de filtrado ---
    encontrados = []

    for pais in paises: 
        superf = pais["superficie"] # superf es superficie
        if rango_min <= superf <= rango_max:
            encontrados.append((pais["pais"], superf, pais["continente"]))

    # --- Imprimir resultados ---
    if encontrados:
        for pais in encontrados:
            print(f"País: {pais[0]}, Superficie: {pais[1]}, Continente: {pais[2]}")
    else:
        print(f"No hay ningún país con un rango de superficie entre {rango_min} y {rango_max}")