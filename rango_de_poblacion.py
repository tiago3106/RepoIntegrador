from validaciones import validar_numero
import re

def rango_de_poblacion(paises):
    """Filtra países por rango de población. 'paises' es la lista devuelta por lista_pais()."""
    # pedir y validar rango mínimo
    while True:
        entrada_min = input("Ingrese el rango mínimo de población de los países buscados: ").strip()
        min_val = validar_numero(entrada_min)
        if min_val is not None:
            break
        print("Ingrese un número válido para el mínimo.")
    # pedir y validar rango máximo
    while True:
        entrada_max = input("Ingrese el rango máximo de población de los países buscados: ").strip()
        max_val = validar_numero(entrada_max)
        if max_val is not None:
            break
        print("Ingrese un número válido para el máximo.")

    if min_val > max_val:
        min_val, max_val = max_val, min_val

    print(f'Los países que se encuentran entre {min_val} y {max_val} son:')

    datos = paises[1:] if len(paises) > 1 else []
    encontrados = []

    for row in datos:
        if len(row) > 2:
            raw = row[2].strip()
            # eliminar todo lo que no sea dígito para manejar comas, puntos, espacios
            digits = re.sub(r'\D', '', raw)
            if not digits:
                continue
            pobl = int(digits)
            if min_val <= pobl <= max_val:
                nombre = row[0].strip().title() if len(row) > 0 else ""
                continente = row[1].strip().title() if len(row) > 1 else ""
                encontrados.append((nombre, pobl, continente))

    if encontrados:
        for nombre, pobl, continente in encontrados:
            print(f"{nombre} - Población: {pobl} - Continente: {continente}")
    else:
        print(f"No hay ningún país con un rango de población entre {min_val} y {max_val}")

def maximo_minimo_datos(paises):
    """Devuelve (minimo, maximo) de poblaciones encontradas en 'paises'."""
    import re
    datos = paises[1:] if len(paises) > 1 else []
    poblaciones = []
    for row in datos:
        if len(row) > 2:
            raw = row[2].strip()
            digits = re.sub(r'\D', '', raw)
            if not digits:
                continue
            poblaciones.append(int(digits))
    if not poblaciones:
        return 0, 0
    return min(poblaciones), max(poblaciones)
