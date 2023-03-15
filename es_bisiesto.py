def es_bisiesto(anio):
    if anio % 4 != 0 and anio % 400 != 0:
        return f"{anio} No es bisiesto"
    elif anio % 100 != 0:
       return f"{anio} Es bisiesto"
    else:
        return f"{anio} Es bisiesto"
    
print(es_bisiesto(2024))