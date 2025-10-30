from manejo_de_archivos import lista_pais
from filtrar_continente import continente_filtrado

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
            continente_filtrado(paises)
        case 2:
            None         


                    


