from validaciones import pedir_nombre, validar_numero
def modificar_pais(nombre_archivo):
    with open (nombre_archivo, "r", encoding="utf-8") as archivo:
        nombre = pedir_nombre(" pais a modificar")
        for linea in archivo:
            if nombre == linea.split(",")[0]:
                continente = pedir_nombre(" nuevo continente")
                superficie = validar_numero(input("ingrese la nueva superficie del pais: "))
                poblacion = validar_numero(input("ingrese la nueva poblacion del pais: "))
            else:
                print("el pais no se encuentra en la lista")
    with open (nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}")
    return archivo