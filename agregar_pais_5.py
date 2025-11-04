from validaciones import validar_numero, pedir_nombre
def agregar_pais(nombre_archivo):
    nombre = pedir_nombre(" pais")
    continente = pedir_nombre(" continente")
    superficie = validar_numero(input("ingrese la superficie del pais: "))
    poblacion = validar_numero(input("ingrese la poblacion del pais: "))
    with open (nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}")
