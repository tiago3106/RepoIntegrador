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
    while bucle: #bucle para buscar un archivo por su nombre o crear uno nuevo
        archivo_paises = input("Ingrese el nombre del archivo con los datos de los paises: ")
        if not archivo_paises.endswith(".csv"): #verifica que el archivo tenga extension .csv
            archivo_paises += ".csv"
        bucle = verificar_existencia_archivo(archivo_paises) #llama a la funcion verificar_existencia_archivo
        if bucle == False:
            print("Archivo cargado correctamente.") 
        else:
            while continuar:
                elecion = input("(1) ingresar otro nombre  o (2) crear un nuevo archivo con el nombre ingresado: ")
                numero_validado = validar_numero(elecion)
                if elecion == 2:
                    crear_archivo(archivo_paises)
                    bucle = False
                    break
                elif elecion == 1:
                    continuar = True    
                else:
                    print("Opción inválida reingrese el nombre.")
        print(archivo_paises)
    return archivo_paises

def lista_pais(archivo_paises):
    paises=[]
    with open(archivo_paises, 'r', encoding='utf-8') as nuevo_archivo:
        for linea in nuevo_archivo:
            linea_limpia= linea.strip().lower()
            paises.append(linea_limpia.split(','))
    return paises        