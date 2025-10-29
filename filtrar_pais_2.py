from manejo_de_archivos import lista_pais
from validaciones import validar_numero
#filtrar paises por continente, rango de poblacion o rango de superficie
def filtrar(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    opcion=input("""Ingrese la opción deseada: 
                1.Filtrar paises por continente
                2.Fitrar por rango de población
                3.Filtrar por rango de superficie """)
    opcion = validar_numero(opcion)
    match opcion:
        case 1:
            continente=input("Ingrese el continente a filtrar: ").lower()
            for linea in paises:
                if linea[3] == continente:
                    print(linea)
            
    # for linea in paises:
    #     if linea[0] == pais_encontrar:
    #         print(linea)
    #         break