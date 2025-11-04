#validaciones
def validar_numero(caracteres):

    try:
        valor = int(caracteres)
        if valor < 0:
            print('Ingrese un número positivo')
        else: 
            return valor
    except ValueError: 
        print('Carácter inválido, ingrese solo números')
def validar_indice(lista,indice):
    try:
        lista[indice]
    except IndexError:
        print('Índice inválido, fuera de rango')
def normalizar_nombre(t):
    titulo = (t.strip()).lower()
    return t


def nombre_valido(t: str) -> bool:
    titulo = normalizar_nombre(t)
    if titulo == 0:
        return False
    else:
        return True


def pedir_nombre(tipo):
    while True:
        titulo = input(f"ingrese el nombre{tipo}: ")
        condicion = nombre_valido(titulo) #llama la funcion titulo valido que devuelve true  si existe
        if condicion == True:
            break
    return titulo 

#agregar que validaciones haran falta
#formas de traer una funcion de otro archivo
#from nombre_del_archivo import nombre_de_la_funcion
#import nombre_del_archivo