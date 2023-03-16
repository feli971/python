class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def get_resultado(self):
        if self.nota <=6:
            print("la nota de ", self.nombre, "es de:", self.nota,",",self.nombre, ",", "ha desaprobado")
        if self.nota >=7:
            print("la nota de ", self.nombre, "es de:", self.nota,",",self.nombre, "ha aprobado !!")

a = Alumno("Felipe", 10)
a.imprimir_datos()
a.get_resultado()

a2 = Alumno("Georgina", 4)
a2.imprimir_datos()
a2.get_resultado()
