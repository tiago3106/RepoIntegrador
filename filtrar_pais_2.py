#Función principal de filtrado
from filtrar_por_rangos.rango_de_poblacion import rango_de_poblacion
from filtrar_por_rangos.rango_de_superficie import rango_de_superficie
from validaciones import validar_numero 

def filtrar(paises):
    """Menú principal para filtrar la lista de países (lista de dicts)."""
    opcion = validar_numero(input("""Ingrese la opción deseada: 
                        1. Filtrar paises por continente
                        2. Filtrar por rango de población
                        3. Filtrar por rango de superficie 
                        """))
    match opcion:
        case 1:
            continente_buscado = input("Ingrese el continente a filtrar: ").strip().lower()
            if not continente_buscado:
                print("Búsqueda cancelada.")
                return
            print(f'Los paises cuyo continente comienza con "{continente_buscado}" son:')
            encontrados = []

            for pais in paises: 
                continente_del_pais = pais["continente"].lower()
                if continente_del_pais.startswith(continente_buscado): 
                    encontrados.append(pais)
            if encontrados:
                for pais in encontrados:
                    # Imprimimos el nombre y el continente 
                    print(f"- País: {pais['pais']}, Continente: {pais['continente']}, Población: {pais['poblacion']}, Superficie: {pais['superficie']}")
            else:
                print(f"No se encontraron países cuyo continente comience con '{continente_buscado}'.")
        case 2:
            rango_de_poblacion(paises)
        case 3:
            rango_de_superficie(paises)
        case _:
            print("Opción no válida")
