from funcion_menu import menu
from manejo_de_archivos import buscar_archivos, lista_pais, guardar_en_archivo 
from buscar_pais_1 import buscar_pais
from filtrar_pais_2 import filtrar
from validaciones import validar_numero
from Ordenamiento_principal_3 import ordenamiento_principal
from Estadisticas_paises_4 import Estadisticas_generales
from agregar_pais_5 import agregar_pais
from modificar_pais_6 import modificar_pais

nombre_archivo = buscar_archivos()
paises = lista_pais(nombre_archivo)
# Variable para ver si modificamos la lista 'paises'
cambios_sin_guardar = False

while True:
    # Llama a la funcion menu que muestra las opciones
    opcion = validar_numero(menu())
    match opcion:
        case 1:
            # buscar un país 
            buscar_pais(paises)
        case 2:
            # filtrar paises 
            filtrar(paises)
        case 3:
            ordenamiento_principal(paises)
        case 4:
            # mostrar estadisticas
            Estadisticas_generales(paises)
        case 5:
            # agregar pais
            agregar_pais(paises)
            cambios_sin_guardar = True # Marcamos que hay cambios
            print("INFO: País agregado a la memoria. Guarde para actualizar el archivo.")
        case 6: 
            # modificar pais
            modificar_pais(paises)
            cambios_sin_guardar = True # Marcamos que hay cambios
            print("INFO: País modificado en memoria. Guarde para actualizar el archivo.")
            
        case 7:
            #Guardar cambios en el archivo
            print("Guardando cambios en el archivo...")
            if guardar_en_archivo(nombre_archivo, paises):
                cambios_sin_guardar = False # Reseteamo la bandera si se guardó
            
        case 8:
            if cambios_sin_guardar:
                confirmar = input("Hay cambios sin guardar. ¿Desea guardar antes de salir? (s/n): ").strip().lower()
                if confirmar == 's':
                    print("Guardando cambios en el archivo...")
                    if guardar_en_archivo(nombre_archivo, paises):
                        print("Cambios guardados. Saliendo del programa.")
                else:
                    print("Saliendo sin guardar los cambios.")
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida, por favor intente de nuevo.")