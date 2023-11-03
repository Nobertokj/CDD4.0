class Animal:
    def __init__(self, nome, cor, som):
        self.nome = nome
        self.cor = cor
        self.som

    def comer(self):
        print(f"O {self.nome} foi comer...")

    def som (self):
        print(f"O {self.nome} foi {self.som}")

class Gato(Animal):
    def __init__(self, nome, cor, som):
        super().__init__(nome, cor, som)

    def som(self):
        print(f"{self.nome} foi miando")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f'{self.nome} foi mugindo')

class coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} foi chiando")