from manejo_de_archivos import lista_pais
#buscar un país por el nombre
def buscar_pais(nombre_archivo):
    paises= lista_pais(nombre_archivo)

    pais_encontrar= input('Ingrese el país que desea encontrar: ').lower()
    for linea in paises:
        if linea[0] == pais_encontrar:
            print(linea)
            break


