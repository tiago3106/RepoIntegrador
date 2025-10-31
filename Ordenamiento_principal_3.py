#Función principal de ordenamiento 
from ordenamiento_poblacion import poblacion_ordenada
from ordenamiento_nombre import nombre_ordenado
from ordenamiento_superficie_acendente import superficie_ascendente
from manejo_de_archivos import lista_pais
from validaciones import validar_numero
from oedenamiento_superficie_descendente import superficie_descendente
def ordenamiento_principal(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    # Se le pregunta al usuario que opcion desea
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
            decision=input('1.Orden ascedente o 2.Orden descendente: ')
            if decision == '1':
                superficie_ascendente(paises) #Se ordenan los paises por superficie ascendente
            elif decision == '2':
                superficie_descendente(paises) #Se ordenan os paises por superficie descendente