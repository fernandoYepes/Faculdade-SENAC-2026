from no import No 

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


    def imprimirPreOrdem(srelf, raiz : No):
        if raiz is not None:
            print( raiz.dado, end = " - ")
            self.imprimirEmOrdem( raiz.esq )
            self.imprimirEmOrdem( raiz.dir )