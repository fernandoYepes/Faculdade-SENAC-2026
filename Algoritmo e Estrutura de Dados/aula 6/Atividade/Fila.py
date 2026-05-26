from Apartamento import Apartamento

class Fila:
    def _init_(self):
        self.inicio = None
        self.fim = None

    def add(self, ap):
        if self.inicio is None:
           self.inicio = ap
        else:
            self.fim.prox = ap
        self.fim = ap

    def imprimir(self):
        print("-----------")
        if self.inicio is None:
            print("Fila de Apartamentos vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux )
                aux = aux.prox
    
    def remover(self):
        if self.inicio is None:
            print("Não há apartamentos na fila")
        else:
            aux = self.inicio
            self.inicio = self.inicio.prox
            del ( aux )
            if self.inicio is None:
                self.fim = None