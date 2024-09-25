class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        return area
         # implementación de la función con la forula de área de un rectángulo


class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio
         # inicialización de la variable radio

    def area(self):
        area = self.pi * self.radio**2
        return area
         # implementación de la función con la forula de área de un círculo


rectangulo = Rectangulo(4,5)
rectArea=rectangulo.area()
print(rectArea)

circulo = Circulo(3)
circArea=circulo.area()
print(circArea)