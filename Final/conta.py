from abc import ABC, abstractmethod   #ABC permite criar uma classe abstrata
from transacao import Transacao

class Conta(ABC):        # Classe responsável pelas operações bancárias
    @abstractmethod      # indica que o construtor deverá ser implementado pelas classes filhas
    def __init__(self, numero, cliente, tipo):
        self.numero = numero
        self.cliente = cliente
        self.tipo = tipo
        self.saldo = 0.0
        self.historico_transacoes = []
        self.historico_saldos = [0.0]

    def depositar(self, valor):                         # Depositar
        if valor > 0:
            self.saldo += valor
            transacao = Transacao("DEPOSITO", valor)    # criamos um objeto transação do tipo deposito
            self.historico_transacoes.append(transacao)
            self.historico_saldos.append(self.saldo)
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("O valor do depósito deve ser positivo.")
            return False
    
    
    def sacar(self, valor):                                # Sacar
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return False
        elif valor <= self.saldo:
            self.saldo -= valor
            transacao = Transacao("SAQUE", valor)          # Criamos um objeto transação do tipo saque
            self.historico_transacoes.append(transacao)
            self.historico_saldos.append(self.saldo)
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Saldo insuficiente.")
            return False


    def mostrar_historico(self):
        return self.historico_transacoes

    def exibirHistoricoSaldo(self):
        return self.historico_saldos

    def transferir(self, conta_destino, valor):                     # transferir
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
            transacao_saida = Transacao("TRANSFERENCIA_ENVIADA", valor)
            transacao_entrada = Transacao("TRANSFERENCIA_RECEBIDA", valor)
            self.historico_transacoes.append(transacao_saida)
            conta_destino.historico_transacoes.append(transacao_entrada)
            self.historico_saldos.append(self.saldo)
            conta_destino.historico_saldos.append(conta_destino.saldo)
            print("Transferência realizada com sucesso!")
            return "sucesso"
