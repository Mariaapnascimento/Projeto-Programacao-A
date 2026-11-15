from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, taxaManutencao):
        super().__init__(numero, cliente, "Corrente")
        self.taxaManutencao = taxaManutencao

    def DescontarTaxa(self):
        if self.taxaManutencao <= 0:
            print("A taxa de manutenção deve ser positiva.")
            return False
        elif self.taxaManutencao > self.saldo:
            print("Saldo insuficiente para descontar a taxa.")
            return False
        else:
            self.saldo -= self.taxaManutencao
            self.historico_saldos.append(self.saldo)
            self.historico_transacoes.append(
                f"Taxa de manutenção: R$ {self.taxaManutencao:.2f}"
            )
            print("Taxa de manutenção descontada com sucesso!")
            return True


