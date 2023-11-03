class Pessoa:
    def __init__(self, nome, peso, idade, comendo= False, dormindo= False, falando = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando

    def apesentar(self):
        print(f"Olá, meu nome é {self.nome}! Eu tenho {self.idade} anos e peso {self.peso}KG :)")

    def comer(self, comida):
        if self.comendo == True:
            print(f" {self.nome} não pode bater o sarro pois já está batendo o sarro.")
        elif self.dormindo == True:
            print (f"{self.nome} não pode bater o sarro pois está tirando um ronco.")
        else:
            self.alimento == comida
            print(f"{self.nome} começou a comer {self.alimento}")
            self.comendo==True

    def parouacomida (self):
        if self.comer == True:
            print(f"{self.nome} parou de comer {self.alimento}")
            self.comendo== False
        else:
            print(f"{self.nome} não está comendo.")

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} Não pode hablar pois já está hablando #yesQueen.")
        elif self.comendo == True:
            print(f"{self.nome} não pode hablar pois está batendo o sarro.")
        elif self.dormindo == True:
            print(f"{self.nome} não pode hablar pois está tirando um ronco.")
        else:
            print(f"{self.nome} começou a hablar #habla_mais_lenda!!! ")
            self.falando==True

    def se_calou (self):
        if self.falando == True:
            print(f"ninguem aguentou o lacre e {self.nome} teve q se calar")
            self.falando== False
        else:
            print(f"{self.nome} não esta dando feche em ninguem.")

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} não pode tirar um ronco pois já esta fazendo.")
        elif self.falando == True:
            print(f"{self.nome} não pode tirar um ronco pois está hablando d+ (arrasa lenda!)")
        elif self.comendo == True:
            print(f"{self.nome} Não pode tirar um ronco pois está batendo o sarro.")
        else:
            print(f"{self.nome} foi de comes (foi mimir)!")
            self.dormindo == True

    def acordou (self):
        if self.dormindo == True:
            print(f"{self.nome} parou de mimir.")
            self.dormindo== True
        else:
            print(f"{self.nome} não está dormindo")

