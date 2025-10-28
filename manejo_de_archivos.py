import csv
from validaciones import validar_numero
def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as nuevo_archivo:
        encabezado = "Nombre,Continente,Poblacion,Superficie\n"
        nuevo_archivo.write(encabezado)
    print(f"Archivo {nombre_archivo} creado correctamente.")

def verificar_existencia_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Si el archivo se abre correctamente, salimos del bucle
            bucle = False
            return bucle
    except FileNotFoundError:
        print("El archivo no existe. Por favor, ingrese un nombre de archivo ya existente.") 

def buscar_archivos():           
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
    return archivo_paises

def lista_pais(archivo_paises):
    paises=[]
    with open(archivo_paises, 'r', encoding='utf-8') as nuevo_archivo:
        for linea in nuevo_archivo:
            linea_limpia= linea.strip().lower()
            paises.append(linea_limpia.split(','))
    return paises        