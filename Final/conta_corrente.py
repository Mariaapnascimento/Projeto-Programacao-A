from conta import Conta
from transacao import Transacao

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente, "Corrente")
        self.taxaManutencao = 5.00
        self.ultimo_desconto = None

    def DescontarTaxa(self):
        if self.taxaManutencao > self.saldo:
            print("Saldo insuficiente para descontar a taxa.")
            return False

        self.saldo -= self.taxaManutencao
        self.historico_saldos.append(self.saldo)

        transacao = Transacao("TAXA_MANUTENCAO", self.taxaManutencao)
        self.historico_transacoes.append(transacao)
        self.ultimo_desconto = transacao.data
        print("Taxa de manutenção descontada com sucesso!")
        return True











