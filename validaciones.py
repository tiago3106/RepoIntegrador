# --- validaciones.py (Corregido) ---
def validar_numero(caracteres):
    """
    Intenta convertir una cadena en un entero positivo.
    Devuelve el entero si es exitoso.
    Devuelve None si es inválido (no numérico, vacío o negativo).
    """
    try:
        valor = int(caracteres)
        if valor < 0:
            print('Error: Ingrese un número positivo.')
            return None
        else: 
            return valor
    except ValueError: 
        if len(caracteres) == 0:
            print('Error: No ingresó ningún valor.')
        else:
            print('Error: Carácter inválido, ingrese solo números.')
            
        return None # Retornar None en caso de error

# --- Validación de Nombres (Corregido) ---

def normalizar_nombre(t: str) -> str:
    """
    Limpia un string: quita espacios y lo pone en formato Título.
    """
    titulo = (t.strip()).title() 
    #Devolver la variable 'titulo' normalizada
    return titulo

def nombre_valido(t: str) -> bool:
    """
    Verifica si un nombre es válido (no está vacío después de limpiarlo).
    """
    titulo_normalizado = normalizar_nombre(t)
    # Devuelve True si la longitud es mayor que 0
    return len(titulo_normalizado) > 0

def pedir_nombre(tipo: str) -> str:
    """
    Pide un nombre (ej. 'pais' o 'continente') hasta que sea válido.
    Devuelve el nombre normalizado.
    """
    while True:
        titulo_raw = input(f"Ingrese el nombre{tipo}: ").strip()
        # 1. Validamos el nombre
        if nombre_valido(titulo_raw):
            titulo_final = normalizar_nombre(titulo_raw)
            break
        else:
            print(f"Nombre inválido. {tipo} no puede estar vacío.")
    # 3. CORRECCIÓN: Devolvemos la versión FINAL, normalizada
    return titulo_final