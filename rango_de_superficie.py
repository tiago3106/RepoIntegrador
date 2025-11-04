from validaciones import validar_numero
import re

def rango_de_superficie(paises):
    """Filtra países por rango de superficie. 'paises' es la lista devuelta por lista_pais()."""
    # pedir y validar rango mínimo
    while True:
        entrada_min = input("Ingrese el rango mínimo de superficie de los países buscados: ").strip()
        min_val = validar_numero(entrada_min)
        if min_val is not None:
            break
        print("Ingrese un número válido para el mínimo.")
    # pedir y validar rango máximo
    while True:
        entrada_max = input("Ingrese el rango máximo de superficie de los países buscados: ").strip()
        max_val = validar_numero(entrada_max)
        if max_val is not None:
            break
        print("Ingrese un número válido para el máximo.")

    if min_val > max_val:
        min_val, max_val = max_val, min_val

    print(f'Los países que se encuentran entre {min_val} y {max_val} de superficie son:')

    datos = paises[1:] if len(paises) > 1 else []
    encontrados = []

    for row in datos:
        # CSV esperado: nombre,poblacion,superficie,continente -> superficie en índice 2
        if len(row) > 2:
            raw = row[2].strip()
            # eliminar todo lo que no sea dígito para manejar comas, puntos, espacios
            digits = re.sub(r'\D', '', raw)
            if not digits:
                continue
            superficie = int(digits)
            if min_val <= superficie <= max_val:
                nombre = row[0].strip().title() if len(row) > 0 else ""
                continente = row[3].strip().title() if len(row) > 3 else ""
                encontrados.append((nombre, superficie, continente))

    if encontrados:
        for nombre, superficie, continente in encontrados:
            print(f"{nombre} - Superficie: {superficie} - Continente: {continente}")
    else:
        print(f"No hay ningún país con un rango de superficie entre {min_val} y {max_val}")


def maximo_minimo_superficie(paises):
    """Devuelve (minimo, maximo) de superficies encontradas en 'paises'."""
    datos = paises[1:] if len(paises) > 1 else []
    superficies = []
    for row in datos:
        if len(row) > 2:
            raw = row[2].strip()
            digits = re.sub(r'\D', '', raw)
            if not digits:
                continue
            superficies.append(int(digits))
    if not superficies:
        return 0, 0
    return min(superficies), max(superficies)
