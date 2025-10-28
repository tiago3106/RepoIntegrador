#validaciones
def validar_numero(caracteres):
    try:
        valor = int(caracteres)
        condicion = True
    except ValueError: 
        print('Carácter inválido, ingrese solo números')
        condicion = False
    return condicion


#agregar que validaciones haran falta
#formas de traer una funcion de otro archivo
#from nombre_del_archivo import nombre_de_la_funcion
#import nombre_del_archivo