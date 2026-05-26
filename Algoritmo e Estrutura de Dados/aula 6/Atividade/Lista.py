from Apartamento import Apartamento

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("---------------")
        print("Lista de Apartamentos por ordem da vaga")
        if self.inicio is None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux: 
                print( aux )
                aux = aux.prox
    
    def add(self, ap):
    
        if self.inicio == None: 
            self.inicio = ap
        else:
            if ap.vaga < self.inicio.vaga:
            ap.proximo = self.inicio
            self.inicio = ap
                else:
                    ant = self.inicio
                    aux = self.inicio.prox
                    while aux:
                    if ap.vaga < aux.vaga:
                        ap.prox = aux
                        ant.proximo = ap
                        break
                    else:
                        ant = aux
                        aux = aux.prox

                    if aux == None:
                        ant.proximo = ap

                self.imprimir()
