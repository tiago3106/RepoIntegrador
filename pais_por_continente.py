def cant_pais_por_continente(paises):
    #Asia
    cont_asia=0
    saltar_encabezado=paises[1:]
    for linea in saltar_encabezado:
        if linea[3].lower()=='asia':
            cont_asia+=1
    print(f'La cantidad de paises que se encuentran en Asia es de : {cont_asia} paises')
    #América
    cont_america=0
    for linea in saltar_encabezado:
        if linea[3].lower()=='américa':
            cont_america+=1
    print(f'La cantidad de paises que se encuentran en América es de : {cont_america} paises')
    #Europa
    cont_europa=0
    for linea in saltar_encabezado:
        if linea[3].lower()=='europa':
            cont_europa+=1
    print(f'La cantidad de paises que se encuentran en Europa es de : {cont_europa} paises')
    #África
    cont_africa=0
    for linea in saltar_encabezado:
        if linea[3].lower()=='áfrica':
            cont_africa+=1
    print(f'La cantidad de paises que se encuentran en África es de : {cont_africa} paises')
    #Oceanía
    cont_oceania=0
    for linea in saltar_encabezado:
        if linea[3].lower()=='oceanía':
            cont_oceania+=1
    print(f'La cantidad de paises que se encuentran en Oceanía es de : {cont_oceania} paises')
    
