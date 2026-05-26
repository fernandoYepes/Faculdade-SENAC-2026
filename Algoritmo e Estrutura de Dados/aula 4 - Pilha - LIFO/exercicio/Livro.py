from Autor import Autor

class Livro:

    def _init_(self, titulo, paginas = 0, autor = Autor() ):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor
        self.prox = None

    def __str__(self):
        txt = "\nTitulo: " + self.titulo
        txt += "\nPáginas: " + str( self.paginas )
        txt += "\n" + str( self.autor)
        return txt