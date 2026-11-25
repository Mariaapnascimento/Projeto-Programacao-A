from conta import Conta
from transacao import Transacao

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente, "Poupança")
        self.taxaRendimento = 5.0
        self.ultimo_rendimento = None

    def AplicarRendimento(self):
        if self.saldo <= 0:
            print("Não há saldo para aplicar rendimento.")
            return False

        rendimento = self.saldo * (self.taxaRendimento / 100)
        self.saldo += rendimento
        self.historico_saldos.append(self.saldo)

        transacao = Transacao("RENDIMENTO", rendimento)
        self.historico_transacoes.append(transacao)
        self.ultimo_rendimento = transacao.data

        print("Rendimento aplicado com sucesso!")
        return True
