class ContaBanco:
    def __init__(self, numero, saldo, tipo, nome, status = False):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo
        self.status = status
        self.nome = nome
        self.limite = 0

    def ativarConta (self):
        if self.status == False:
            print('A conta foi ativada')
            self.status = True
        else:
            print ('A conta ja está ativada')

    def  ativarLimite (self, valorLimite):
        if self.limite == 0:
            print(f"foi adicionado limite de R${self.limite * -1}")
            self.limite = valorLimite * -1
        else:
            print("o limite da conta já foi ativado")

    def depositar (self, valorDeposito):
        if valorDeposito > 0:
            self.saldo += valorDeposito
            print(f" o valor de R${valorDeposito} foi adicionado a conta.")
        else:
            print("Valor de deposito muito baixo.")

    def sacar (self, valorSaque):
        if (self.saldo-valorSaque)> self.limite:
            print(f"Foi sacado o valor de: R${valorSaque}")
            self.saldo -= valorSaque
        else:
            print("O valor sacado é maior do que o limite da conta.")

    def verificarSaldo (self):
        if self.saldo>0:
            print(f"o seu saldo é de: R${self.saldo}\n Seu limite é de: R${self.limite*-1}")
        else:
            print(f"O seu saldo é de: R$0 \n você possui um limite de: R${self.limite - self.saldo}")