from funcion_menu import menu
from validaciones import verificar_existencia_archivo
from manejo_de_archivos import crear_archivo  
bucle = True
continuar = True
while bucle: #bucñe para buscar un archivo por su nombre o crear uno nuevo
    archivo_paises = input("Ingrese el nombre del archivo de paises (con extension .csv): ")
    if archivo_paises.endswith(".csv"): #verifica que el archivo tenga extension .csv
        bucle = verificar_existencia_archivo(archivo_paises) #llama a la funcion verificar_existencia_archivo
        if bucle == False:
            print("Archivo cargado correctamente.") 
        else:
            while continuar:
                elecion = input("(1) intente nuevamente. o (2) desea crear un nuevo archivo con ese nombre: ")
                validar_numero = validar_numero(elecion)
                if validar_numero and int(elecion) == 2:
                    crear_archivo(archivo_paises)
                    bucle = False
                    continuar = False
                elif validar_numero and int(elecion) == 1:
                    continuar = True    
                else:
                    print("Opción inválida reiniciando pedido de archivo.")
                    
    else:
        print("El archivo debe tener extension .csv. Intente nuevamente.")
bucle = True
while bucle:
    opcion = menu() #llama a la funcion menu que esta en el funcion_menu.py
    match opcion:
        case "1":
            #buscar un país por el nombre
            None
        case "2":
            #filtrar paises por continente, rango de poblacion o rango de superficie
            None
        case "3":
            #ordenar paises por nombre, poblacion o superficie(aascedente o descendente)
            None
        case "4":
            #mostrar estadisticas de los paises por pais con mayor o menor poblacion, promedio de poblacion, pais con mayor o menor superficie
            #promediode superficie, cantidad de paises por continente
            None
        case "5":
            #agregar pais
            None
        case "6":   
            #modificar pais
            None
        case "7":
            bucle = False