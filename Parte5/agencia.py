class Agencia:          # Classe responsável por administrar as contas da agência
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.contas = []

    def adicionar_conta(self, conta):
        for conta_cadastrada in self.contas:
            if conta_cadastrada.numero == conta.numero:
                print("Essa conta já está cadastrada na agência.")
                return
        self.contas.append(conta)
        print("Conta adicionada à agência com sucesso!")

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_contas(self):
        if len(self.contas) == 0:
            print("Nenhuma conta cadastrada.")
        else:
            print("\n### CONTAS CADASTRADAS ###")
            for conta in self.contas:
                print("----------------------------")
                print(f"Cliente: {conta.cliente.nome}")
                print(f"Conta: {conta.numero}")
                print(f"Tipo: {conta.tipo}")
                print(f"Saldo: R$ {conta.saldo:.2f}")

    def calcular_patrimonio_total(self):
        total = 0.0
        for conta in self.contas:
            total += conta.saldo
        return total
    
