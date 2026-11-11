from cliente import Cliente

class Conta:       # Classe responsável pelas operações bancárias
    def __init__(self, numero, cliente, tipo):
        self.numero = numero
        self.cliente = cliente
        self.tipo = tipo
        self.saldo = 0.0
        self.historico_transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico_transacoes.append(
                f"Depósito: R$ {valor:.2f}"
            )
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("O valor do depósito deve ser positivo.")
            return False
    
    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return False
        elif valor <= self.saldo:
            self.saldo -= valor
            self.historico_transacoes.append(
                f"Saque: R$ {valor:.2f}"
            )
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def mostrar_historico(self):
        return self.historico_transacoes

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            print("O valor da transferência deve ser positivo.")
            return "valor_invalido"
        elif self is conta_destino:
            print("Não é possível transferir para a mesma conta.")
            return "mesma_conta"
        elif valor > self.saldo:
            print("Saldo insuficiente.")
            return "saldo_insuficiente"
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico_transacoes.append(
                f"Transferência enviada para a conta "
                f"{conta_destino.numero}: R$ {valor:.2f}"
            )
            conta_destino.historico_transacoes.append(
                f"Transferência recebida da conta "
                f"{self.numero}: R$ {valor:.2f}"
            )
            print("Transferência realizada com sucesso!")
            return "sucesso"
