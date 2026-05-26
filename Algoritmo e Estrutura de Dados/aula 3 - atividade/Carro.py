class Carro:

    def _init_(self, modelo = None, placa = None, ano = 2026):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.prox = None
    
    def _str_(self):
        txt = "\nModelo: " + self.modelo
        txt = "\nPlaca: " + self.placa
        txt = "\nAno: " + str(self.ano)
        return txt
        