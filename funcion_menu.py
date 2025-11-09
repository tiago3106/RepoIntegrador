from validaciones import validar_numero

def menu(): 
    """
    Muestra el menú, valida la entrada y devuelve una opción válida.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar un país")
        print("2. Filtrar un país")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Agregar país")
        print("6. Modificar país")
        print("7. Guardar cambios en el archivo")
        print("8. Salir") 
        opcion_str = input("Seleccione una opción (1-8): ")
        opcion = validar_numero(opcion_str)
        #Chequeo de 'None' (evita el TypeError)
        if opcion is None:
            # validar_numero ya imprimió el error (ej. "solo números" o "valor vacío")
            # Así que simplemente pedimos de nuevo
            continue 
        if 1 <= opcion <= 8:
            return opcion 
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")