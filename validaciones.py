#validaciones
def validar_numero(caracteres):
    try:
        valor = int(caracteres)
        return valor
    except ValueError: 
        print('Carácter inválido, ingrese solo números')


#agregar que validaciones haran falta
#formas de traer una funcion de otro archivo
#from nombre_del_archivo import nombre_de_la_funcion
#import nombre_del_archivo