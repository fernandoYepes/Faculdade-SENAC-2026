from No import No 
from Fila import Fila

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz : No, valor):
        if raiz is None:
            nodo = No( valor )
            if self.raiz is None:
                self.raiz = nodo
            return nodo
        
        if valor <= raiz.dado:
            raiz.esq = self.inserir(raiz.esq, valor)

        if valor > raiz.dado:
            raiz.dir = self.inserir(raiz.dir, valor)

        return raiz
    
    def imprimirEmOrdem(self, raiz : No):
        if raiz is not None:
            self.imprimirEmOrdem( raiz.esq )
            print ( raiz.dado, end = " - ")
            self.imprimirEmOrdem( raiz.dir )



    def imprimirPreOrdem(self, raiz : No):
        if raiz is not None:
            print( raiz.dado, end = " - ")
            self.imprimirEmOrdem( raiz.esq )
            self.imprimirEmOrdem( raiz.dir )

    def imprimirPosOrdem(self, raiz : No):
        if raiz is not None:
            self.imprimirEmOrdem( raiz.esq )
            self.imprimirEmOrdem( raiz.dir )
            print( raiz.dado, end = " - ")
    
    def imprimirReverso(self, raiz : No):
        if raiz is not None:
            self.imprimirEmOrdem( raiz.dir )
            print( raiz.dado, end = " - ")
            self.imprimirEmOrdem( raiz.esq )

    def imprimirEmNivel(self, raiz: No):
        if raiz == None:
            return
        fila = Fila()
        fila.add( raiz )

        while fila.inicio != None:
            tamanho = fila.tamanho
            for _ in range( tamanho ):
                atual = fila.remover()
                print( atual.dado, end = " - ")

                if atual.esq != None:
                    fila.add( atual.esq )

                if atual.dir != None:
                    fila.add( atual.dir )

            print("")