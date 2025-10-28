from manejo_de_archivos import lista_pais
 #filtrar paises por continente, rango de poblacion o rango de superficie
def filtrar(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    opcion=input("""Ingrese la opción deseada: 
                 1.Filtrar paises por continente
                 2.Fitrar por rango de población
                 3.Filtrar por rango de superficie """)
    match opcion:
        case '1':
            None
    # for linea in paises:
    #     if linea[0] == pais_encontrar:
    #         print(linea)
    #         break