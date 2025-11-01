#Función principal de ordenamiento 
from ordenamiento_poblacion import poblacion_ordenada
from ordenamiento_nombre import nombre_ordenado
from ordenamiento_superficie import superficie_ascendente, superficie_descendente
from manejo_de_archivos import lista_pais
from validaciones import validar_numero,validar_indice
elecion_3  = [superficie_ascendente, superficie_descendente] #para ahorrar lineas de codigo
def ordenamiento_principal(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    # Se le pregunta al usuario que opcion
    # de ordenamiento desea
    print(""" 
        1.Ordenar por nombre
        2.Ordenar por población
        3.Ordenar por superficie(ascedente o descendente)""")
    opciones=int(input('Ingrese la opcion deseada: '))
    validar_numero(opciones)
    match opciones:
        case 1:
            nombre_ordenado(paises) #Se ordenan los paises por nombre 
        case 2:
            poblacion_ordenada(paises) #Se ordenan los paises por población
        case 3:
            decision=validar_numero(input('0.Orden ascedente o 1.Orden descendente: '))
            validar_indice(elecion_3, decision)
            elecion_3[decision - 1] #Se ordenan los paises segun la eleccion del usuario
            