def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def restar(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    if num2 == 0:
        print("No se puede dividir entre cero")
    else:
        resultado = num1 / num2
        return resultado
