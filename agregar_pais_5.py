from validaciones import validar_numero, pedir_nombre
def agregar_pais(paises):
    #Recolectar datos del nuevo país
    nombre = pedir_nombre(" pais")
    continente = pedir_nombre(" continente")
    # 3. Validar los números
    superficie = validar_numero(input("Ingrese la superficie del pais: "))
    if superficie is None:
        print("Entrada inválida. Operación cancelada.")
        return # Salir de la función si la superficie no es válida
    
    poblacion = validar_numero(input("Ingrese la poblacion del pais: "))
    if poblacion is None:
        print("Entrada inválida. Operación cancelada.")
        return # Salir de la función si la población no es válida
    nuevo_pais = {
        "pais": nombre.title(),
        "continente": continente.title(),
        "superficie": superficie,
        "poblacion": poblacion
    }
    # 5. Modificar la lista en MEMORIA
    paises.append(nuevo_pais)
    print(f"Se agregó '{nuevo_pais['pais']}' a la sesión.")
    print("(Recuerda guardar los cambios [Opción 7] para actualizar el archivo).")