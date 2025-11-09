#buscar un país por el nombre
def buscar_pais(paises):
    bandera= False
    pais_encontrar = input('Ingrese el nombre del país que desea encontrar o las iniciales: ').strip().lower()

    # Si la entrada está vacía, no buscamos nada.
    if not pais_encontrar:
        print("Búsqueda cancelada. No se ingresó un nombre.")
        return # Salimos de la función

    for linea in paises:
        if linea['pais'].lower().startswith(pais_encontrar):
            print(f"País encontrado: {linea['pais']}, Población: {linea['poblacion']}, Superficie: {linea['superficie']}, Continente: {linea['continente']}")
            bandera= True
            
    if not bandera: 
        print('El país no se encuentra en la lista')