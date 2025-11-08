#Función principal de filtrado
from manejo_de_archivos import lista_pais
from filtrar_por_rangos.rango_de_poblacion import rango_de_poblacion
from validaciones import validar_numero 
from filtrar_por_rangos.rango_de_superficie import rango_de_superficie
#filtrar paises por continente, rango de poblacion o rango de superficie
def filtrar(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    opcion=validar_numero(input("""Ingrese la opción deseada: 
                1.Filtrar paises por continente
                2.Fitrar por rango de población
                3.Filtrar por rango de superficie
                """))
    match opcion:
        case 1:
            continente=input("Ingrese el continente a filtrar: ").lower()
            print(f'Los paises que se encuentran en {continente} son:')
            for linea in paises: #filtra por continente si tiene la linea mas de 3 elementos y el elemento 3 es igual al continente ingresado
                if len(linea) > 3 and linea[3] == continente:   
                    print(linea)
        case 2:
            rango_de_poblacion(paises)
            #esta en una funcion por que es muy larga
        case 3:
            rango_de_superficie(paises)
            #esta en una funcion por que es muy larga
        case _:
            print("Opción no válida")

