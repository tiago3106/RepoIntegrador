from validaciones import validar_numero
def menu():
    print("1. Buscar un pais.")
    print("2. Filtrar un pais")
    print("3. ordenar paises")
    print("4. Mostrar estadisticas")
    print("5. Agregar pais")
    print("6. moficar pais")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    condicion = validar_numero(opcion)
    if  condicion == False or int(opcion) < 1 or int(opcion) > 7:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")
        return menu()
    return opcion
