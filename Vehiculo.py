class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas     
        self.puertas = puertas   


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


porsche_911 = Coche("Azul", "4", "3", "330", "3996")

print(porsche_911.color, porsche_911.ruedas, porsche_911.puertas, porsche_911.velocidad, porsche_911.cilindrada)


