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
#validar nombre de pais o continente
def normalizar_nombre(t):
    titulo = (t.strip()).lower()
    return t

def nombre_valido(t: str) -> bool:
    titulo = normalizar_nombre(t)
    if len(titulo) == 0:
        return False
    else:
        return True

def pedir_nombre(tipo: str) -> str:
    while True:
        titulo = input(f"ingrese el nombre{tipo}: ")
        condicion = nombre_valido(titulo) #llama la funcion titulo valido que devuelve true  si existe
        if condicion == True:
            break
    return titulo 