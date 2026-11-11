class Cliente:
    def __init__(self, nome, cpf, salario, telefone):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.telefone = telefone


class Conta:
    def __init__(self, numero, cliente, tipo):
        self.numero = numero
        self.cliente = cliente
        self.tipo = tipo
        self.saldo = 0.0
        self.historico_transacoes = []

    def depositar(self, valor):
        if valor <= 0:
            return False, "O valor do depósito deve ser positivo."
        self.saldo += valor
        self.historico_transacoes.append(f"Depósito: R$ {valor:.2f}")
        return True, "Depósito realizado com sucesso!"

    def sacar(self, valor):
        if valor <= 0:
            return False, "O valor do saque deve ser positivo."
        if valor > self.saldo:
            return False, "Saldo insuficiente."
        self.saldo -= valor
        self.historico_transacoes.append(f"Saque: R$ {valor:.2f}")
        return True, "Saque realizado com sucesso!"

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            return False, "O valor da transferência deve ser positivo."
        if self is conta_destino:
            return False, "Não é possível transferir para a mesma conta."
        if valor > self.saldo:
            return False, "Saldo insuficiente."
        self.saldo -= valor
        conta_destino.saldo += valor
        self.historico_transacoes.append(
            f"Transferência enviada para a conta {conta_destino.numero}: R$ {valor:.2f}")
        conta_destino.historico_transacoes.append(
            f"Transferência recebida da conta {self.numero}: R$ {valor:.2f}")
        return True, "Transferência realizada com sucesso!"


class Agencia:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.contas = []

    def adicionar_conta(self, conta):
        if self.buscar_conta(conta.numero) is not None:
            return False, "Essa conta já está cadastrada na agência."
        self.contas.append(conta)
        return True, "Conta adicionada à agência com sucesso!"

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def calcular_patrimonio_total(self):
        return sum(conta.saldo for conta in self.contas)


class Banco:
    def __init__(self, agencia):
        self.clientes = []
        self.agencia = agencia

    def cadastrar_cliente(self, nome, cpf, salario, telefone):
        if self.procurar_cliente(nome) is not None:
            return False, "Esse cliente já está cadastrado."
        self.clientes.append(Cliente(nome, cpf, salario, telefone))
        return True, "Cliente cadastrado com sucesso!"

    def procurar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        return None

    def cadastrar_conta(self, nome, numero, tipo):
        cliente = self.procurar_cliente(nome)
        if cliente is None:
            return False, "Cliente não encontrado."
        return self.agencia.adicionar_conta(Conta(numero, cliente, tipo))

    def procurar_conta(self, numero):
        return self.agencia.buscar_conta(numero)