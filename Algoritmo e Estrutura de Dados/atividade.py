class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimir_informacoes(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas  
    def imprimir_informacoes(self):
        print(f"[Carro] Marca: {self.marca} | Modelo: {self.modelo} | Portas: {self.__portas}")

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtd_helices):
        super().__init__(marca, modelo)
        self._quantidade_de_helices = qtd_helices  # fracamente tipado

    def imprimir_informacoes(self):
        print(f"[Drone] Marca: {self.marca} | Modelo: {self.modelo} | Hélices: {self._quantidade_de_helices}")

class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def vazia(self):
        return len(self.itens) == 0

    def imprimir_pilha(self):
        if self.vazia():
            print("  -> A pilha está vazia.")
        else:
            # (LIFO)
            for item in reversed(self.itens):
                print("  -> ", end="")
                item.imprimir_informacoes()

def menu():
    pilha_carros = Pilha()
    pilha_drones = Pilha()

    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE PILHAS: CARROS E DRONES")
        print("="*40)
        print("1. Add carro à Pilha")
        print("2. Remover carro da Pilha")
        print("3. Add drone à Pilha")
        print("4. Remover drone da Pilha")
        print("5. Imprimir Pilha de carros")
        print("6. Imprimir Pilha de drones")
        print("0. Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            portas = input("Digite a quantidade de portas: ")
            carro = Carro(marca, modelo, portas)
            pilha_carros.adicionar(carro)
            print("Carro adicionado com sucesso no topo da pilha!")

        elif opcao == '2':
            removido = pilha_carros.remover()
            if removido:
                print("Carro removido do topo da pilha:")
                removido.imprimir_informacoes()
            else:
                print("Erro: A pilha de carros já está vazia!")

        elif opcao == '3':
            marca = input("Digite a marca do drone: ")
            modelo = input("Digite o modelo do drone: ")
            helices = input("Digite a quantidade de hélices: ")
            drone = Drone(marca, modelo, helices)
            pilha_drones.adicionar(drone)
            print("Drone adicionado com sucesso no topo da pilha!")

        elif opcao == '4':
            removido = pilha_drones.remover()
            if removido:
                print("Drone removido do topo da pilha:")
                removido.imprimir_informacoes()
            else:
                print("Erro: A pilha de drones já está vazia!")

        elif opcao == '5':
            print("\n--- STATUS DA PILHA DE CARROS (Topo -> Base) ---")
            pilha_carros.imprimir_pilha()

        elif opcao == '6':
            print("\n--- STATUS DA PILHA DE DRONES (Topo -> Base) ---")
            pilha_drones.imprimir_pilha()

        elif opcao == '0':
            print("Fechando prograama...")
            break

        else:
            print("Opção inválida! Tente novamente")

if __name__ == "__main__":
    menu()