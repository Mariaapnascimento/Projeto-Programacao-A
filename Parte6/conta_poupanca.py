from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, taxaRendimento):
        super().__init__(numero, cliente, "Poupança")
        self.taxaRendimento = taxaRendimento

    def AplicarRendimento(self):
        if self.taxaRendimento <= 0:
            print("A taxa de rendimento deve ser positiva.")
            return False
        rendimento = self.saldo * (self.taxaRendimento / 100)
        self.saldo += rendimento
        self.historico_saldos.append(self.saldo)
        self.historico_transacoes.append(
            f"Rendimento: R$ {rendimento:.2f}"
        )
        print("Rendimento aplicado com sucesso!")
        return True

