class Linea:

    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia

    def impresion(self):
        return f"Linea: {self.punto_a.impresion()} -> {self.punto_b.impresion()}"
    
from punto import Punto
p1 = Punto(1, 2)
p2 = Punto(4, 6)

linea = Linea(p1, p2)

print(linea.impresion())

linea.mueve_derecha(3)

print(linea.impresion())

linea.mueve_arriba(2)

print(linea.impresion())