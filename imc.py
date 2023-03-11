peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2)

print("Tu índice de masa corporal es {:.2f}".format(imc))

