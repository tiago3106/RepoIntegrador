import csv
def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as nuevo_archivo:
        encabezado = "Nombre,Continente,Poblacion,Superficie\n"
        nuevo_archivo.write(encabezado)
    print(f"Archivo {archivo_paises} creado correctamente.")
