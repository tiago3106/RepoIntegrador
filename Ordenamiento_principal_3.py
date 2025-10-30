from ordenamiento_poblacion import poblacion_ordenada
from ordenamiento_nombre import nombre_ordenado
from ordenamiento_superficie_acendente import superficie_ascendente
from manejo_de_archivos import lista_pais
def ordenamiento_principal(nombre_archivo):
    paises= lista_pais(nombre_archivo)
    print(""" 
          1.Ordenar por nombre
          2.Ordenar por población
          3.Ordenar por superficie(ascedente o descendente)""")
    opciones=input('Ingrese la opcion deseada: ')
    match opciones:
        case 1:
            nombre_ordenado(paises)
        case 2:
            poblacion_ordenada(paises)
        case 3:
            decision=input('1.Orden ascedente o 2.Orden descendente: ')
            if decision == '1':
                superficie_ascendente(paises)
            elif decision == '2':
                None    




