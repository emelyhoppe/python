class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta", self.numero)
        print("Titular:", self.titular)
        print("Saldo", self.saldo)

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

#aqui estou criando uma instancia do objeto ContaBancaria
#com o nome conta_da_emely

numero_acc = input("Digite o número da sua conta: ")

titular_acc = input("Digite o nomde do titular: ")

saldo_acc = float(input("Digite seu saldo atual: ").replace(",","."))


conta_da_emely = ContaBancaria(numero_acc, titular_acc, saldo_acc)


valor_deposito = float(input("Digite o valor a ser depositado: ").replace(",","."))

valor_saque = float(input("Digite o valor do seu saque: ").replace(",","."))


conta_da_emely.depositar(valor_deposito)

conta_da_emely.sacar(valor_saque)

conta_da_emely.exibir_detalhes()

