#validaciones
def validar_numero(caracteres):
    try:
        valor = int(caracteres)
        condicion = True
    except ValueError:
        condicion = False
    return condicion
def verificar_existencia_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Si el archivo se abre correctamente, salimos del bucle
            bucle = False
            return bucle
    except FileNotFoundError:
        print("El archivo no existe. Por favor, ingrese un nombre de archivo válido.")

#agregar que validaciones haran falta
#formas de traer una funcion de otro archivo
#from nombre_del_archivo import nombre_de_la_funcion
#import nombre_del_archivo