import csv, re
from validaciones import validar_numero

Encabezado = ["pais","poblacion", "superficie", "continente"]

# --- FUNCIONES DE DEPURACIÓN  ---

def _limpiar_numero(valor):
    """Función interna para convertir un valor (str, int, None) a un int limpio."""
    valor_str = str(valor)
    digits = re.sub(r'\D', '', valor_str)
    return int(digits) if digits else 0

def depurar_datos_paises(lista_cruda):
    """
    Devuelve limpia la lista de países. Cada país es un diccionario
    """
    lista_limpia = []
    for pais in lista_cruda:
        nuevo_pais = {} 
        # Leemos 'pais' y lo guardamos como 'pais' (limpiando el valor)
        nuevo_pais['pais'] = pais.get('pais', 'N/A').strip().title()
        nuevo_pais['continente'] = pais.get('continente', 'N/A').strip().title()
        # Limpiamos los números
        nuevo_pais['poblacion'] = _limpiar_numero(pais.get('poblacion'))
        nuevo_pais['superficie'] = _limpiar_numero(pais.get('superficie'))
        lista_limpia.append(nuevo_pais)
    return lista_limpia

# --- FUNCIONES DE MANEJO DE ARCHIVOS (Tu código, actualizado) ---

def crear_archivo(nombre_archivo):
    """Crea un nuevo archivo CSV con el encabezado estándar."""
    with open(nombre_archivo, 'w', newline="", encoding='utf-8') as nuevo_archivo:
        escritor_csv = csv.DictWriter(nuevo_archivo, fieldnames=Encabezado)
        escritor_csv.writeheader() 
    print(f"Archivo {nombre_archivo} creado correctamente.")

def verificar_existencia_archivo(nombre_archivo):
    """Verifica si el archivo existe. Devuelve True o False."""
    try:
        with open(nombre_archivo, 'r', newline="", encoding='utf-8') as archivo:
            return True
    except FileNotFoundError:
        return False

def buscar_archivos(): 
    """Bucle principal para encontrar, cargar o crear un archivo CSV."""
    while True : # Bucle para buscar un archivo
        archivo_paises = input("Ingrese el nombre del archivo de países: ").strip()
        if not archivo_paises.endswith(".csv"):
            archivo_paises += ".csv"
            
        if verificar_existencia_archivo(archivo_paises):
            print("Archivo cargado correctamente.") 
            break # El archivo existe, salimos del bucle
        else:
            print("El archivo no existe.")
            while True: # Bucle para decidir qué hacer
                elecion = input("(1) Ingresar otro nombre o (2) Crear un nuevo archivo: ")
                numero_validado = validar_numero(elecion)

                if numero_validado == 2:
                    crear_archivo(archivo_paises)
                    print("Archivo creado y cargado correctamente.")
                    return archivo_paises
                elif numero_validado == 1:
                    break 
                else:
                    print("Opción inválida. Intente nuevamente.")
    return archivo_paises

def lista_pais(archivo_paises):
    """
    Lee el archivo CSV y devuelve la lista ya limpia.
    """
    paises_crudos = []
    with open(archivo_paises, 'r', newline="", encoding='utf-8') as nuevo_archivo:
        lector_csv = csv.DictReader(nuevo_archivo)
        for fila in lector_csv:
            paises_crudos.append(fila)
    #ya leimos los datos ahora los limpiamos
    paises_limpios = depurar_datos_paises(paises_crudos)
    #Devolvemos la lista limpia.
    return paises_limpios

def guardar_en_archivo(nombre_archivo, paises):
    """
    Sobrescribe el archivo CSV con la lista de países (en memoria).
    """
    try:
        with open(nombre_archivo, 'w', newline="", encoding='utf-8') as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=Encabezado)
            # Escribir el encabezado
            escritor_csv.writeheader()
            # Escribir todas las filas de la lista de países
            for pais in paises:
                escritor_csv.writerow(pais)
                
        print("✅ ¡Cambios guardados correctamente en el archivo!")
        return True # Indica que se guardó
        
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")
        return False # Indica que falló