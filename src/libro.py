class Libro:

    def __init__(self, titulo, autor, isbn, paginas,
                 edicion, editorial, ciudad, pais, fecha_edicion):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion

    # GETTERS

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    # SETTERS

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    # MOSTRAR INFORMACION

    def mostrar_info(self):
        print(f"Titulo: {self.titulo} {self.edicion} edicion")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais})")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} paginas")