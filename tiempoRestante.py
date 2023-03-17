import time
hora_actual = time.localtime().tm_hour
if hora_actual >= 19:
    print("¡Es hora de ir a casa!")
else:
    hora_salida = 19
    minutos_restantes = 60 - time.localtime().tm_min
    segundos_restantes = 60 - time.localtime().tm_sec

    if hora_actual < hora_salida:
        horas_restantes = hora_salida - hora_actual - 1
        minutos_restantes += horas_restantes * 60
    else:
        minutos_restantes += (24 - hora_actual + hora_salida - 1) * 60

    print(f"Aún quedan {minutos_restantes} minutos y {segundos_restantes} segundos de trabajo.")
