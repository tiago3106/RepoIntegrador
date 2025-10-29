#metodos_de_ordenamiento
from manejo_de_archivos import lista_pais

def merge_sort(paises):
    """Ordena una lista de registros [nombre, continente, poblacion, superficie] por nombre y devuelve la lista ordenada."""
    if len(paises) <= 1:
        return paises
    medio = len(paises) // 2
    izquierda = merge_sort(paises[:medio])
    derecha = merge_sort(paises[medio:])
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        # comparar por nombre (posición 0), insensible a mayúsculas/minúsculas
        if str(izquierda[i][0]).lower() <= str(derecha[j][0]).lower():
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    # añadir restos
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ordenar_paises_por_nombre(nombre_archivo):
    """Wrapper: carga los países desde el archivo, ordena y muestra nombre, población y continente."""
    paises = lista_pais(nombre_archivo)
    if not paises:
        print("Archivo vacío o no se pudo leer.")
        return
    # lista_pais actualmente incluye el encabezado como primera línea; omitirlo
    header = paises[0]
    datos = paises[1:]
    if not datos:
        print("No hay datos de países en el archivo.")
        return
    ordenados = merge_sort(datos)
    print("País - Población - Continente (ordenados alfabéticamente):")
    for p in ordenados:
        nombre = p[0].strip().title() if len(p) > 0 else ""
        continente = p[1].strip().title() if len(p) > 1 else ""
        poblacion = p[2].strip() if len(p) > 2 else ""
        print(f"{nombre} - Población: {poblacion} - Continente: {continente}")