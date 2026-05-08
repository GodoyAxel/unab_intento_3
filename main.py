"""NIVEL 1"""
from src.punto import Punto

p1 = Punto(3, 5)

print(p1.eje_x())
print(p1.eje_y())
print(p1.impresion())

p2 = p1.opuesto()

print(p2.impresion())

"""NIVEL 2"""
from src.linea import Linea


p1 = Punto(1, 2)
p2 = Punto(4, 6)

linea = Linea(p1, p2)

print(linea.impresion())

linea.mueve_derecha(3)

print(linea.impresion())

linea.mueve_arriba(2)

print(linea.impresion())

"""NIVEL 3"""
from src.cancion import Cancion


c1 = Cancion("Bohemian Rhapsody", "Queen")

print(c1.get_titulo())
print(c1.get_autor())

c1.set_titulo("Imagine")
c1.set_autor("John Lennon")

print(c1.get_titulo())
print(c1.get_autor())

"""NIVEL 4"""
from src.libro import Libro


libro1 = Libro(
    "Introduction to Java Programming",
    "Liang, Y. Daniel",
    "0-13-031997-X",
    784,
    "3ra",
    "Prentice-Hall",
    "New Jersey",
    "USA",
    "viernes 16 de noviembre de 2001"
)

libro1.mostrar_info()