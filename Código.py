class Cliente:                   # Classe responsável por armazenar os dados do cliente
    def __init__(self, nome, cpf, salario, telefone):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.telefone = telefone

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
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor <= self.saldo:
            self.saldo -= valor
            self.historico_transacoes.append(
                f"Saque: R$ {valor:.2f}"
            )
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def mostrar_historico(self):
        if len(self.historico_transacoes) == 0:
            print("Nenhuma transação realizada.")
        else:
            print("\n### HISTÓRICO DE TRANSAÇÕES ###")
            for transacao in self.historico_transacoes:
                print(transacao)

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            print("O valor da transferência deve ser positivo.")
        elif self is conta_destino:
            print("Não é possível transferir para a mesma conta.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
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

class Banco:
    # Classe responsável pelo cadastro e pela busca de clientes
    # e pela comunicação com a agência
    def __init__(self, agencia):
        self.clientes = []
        self.agencia = agencia

    def cadastrar_cliente(self, nome, cpf, salario, telefone):
        if self.procurar_cliente(nome) is not None:
            print("Esse cliente já está cadastrado.")
            return
        cliente = Cliente(nome, cpf, salario, telefone)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def procurar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        return None

    def cadastrar_conta(self, nome, numero, tipo):
        cliente = self.procurar_cliente(nome)
        if cliente is None:
            print("Cliente não encontrado.")
            return
        conta = Conta(numero, cliente, tipo)
        self.agencia.adicionar_conta(conta)

    def procurar_conta(self, numero):
        return self.agencia.buscar_conta(numero)

    def listar_contas(self):
        self.agencia.listar_contas()

# Criação dos objetos
agencia = Agencia("Agência Central", "003")
banco = Banco(agencia)

while True:     # Menu
    print("\n##### MENU PRINCIPAL #####")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Conta")
    print("3. Listar Contas")
    print("4. Procurar Conta")
    print("5. Consultar Saldo")
    print("6. Depositar")
    print("7. Sacar")
    print("8. Consultar Histórico")
    print("9. Transferir")
    print("10. Consultar Patrimônio Total")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":     # Opção 1 - Cadastrar Cliente
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        salario = float(input("Digite o salário do cliente: "))
        telefone = input("Digite o telefone do cliente: ")
        banco.cadastrar_cliente(nome, cpf, salario, telefone)

    elif opcao == "2":      # Opção 2 - Cadastrar Conta
        nome = input("Digite o nome do cliente: ")
        numero = int(input("Digite o número da conta: "))
        tipo = input("Digite o tipo da conta (Corrente/Poupança): ")
        banco.cadastrar_conta(nome, numero, tipo)

    elif opcao == "3":      # Opção 3 - Listar Contas
        banco.listar_contas()

    elif opcao == "4":      # Opção 4 - Procurar Conta
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)
        if conta is not None:
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Conta: {conta.numero}")
            print(f"Tipo: {conta.tipo}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":      # Opção 5 - Consultar Saldo
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)
        if conta is not None:
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "6":       # Opção 6 - Depositar
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)
        if conta is not None:
            valor = float(input("Valor do depósito: R$ "))
            conta.depositar(valor)
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":        # Opção 7 - Sacar
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)
        if conta is not None:
            valor = float(input("Valor do saque: R$ "))
            conta.sacar(valor)
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "8":       # Opção 8 - Consultar Histórico
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)
        if conta is not None:
            conta.mostrar_historico()
        else:
            print("Conta não encontrada.")

    elif opcao == "9":       # Opção 9 - Transferir
        numero_origem = int(
            input("Digite o número da conta de origem: ")
        )
        numero_destino = int(
            input("Digite o número da conta de destino: ")
        )
        conta_origem = banco.procurar_conta(numero_origem)
        conta_destino = banco.procurar_conta(numero_destino)
        if conta_origem is None or conta_destino is None:
            print("Uma das contas não foi encontrada.")
        else:
            valor = float(
                input("Digite o valor da transferência: R$ ")
            )
            conta_origem.transferir(conta_destino, valor)
            print(
                f"Saldo da conta de origem: "
                f"R$ {conta_origem.saldo:.2f}"
            )
            print(
                f"Saldo da conta de destino: "
                f"R$ {conta_destino.saldo:.2f}"
            )

    elif opcao == "10":        # Opção 10 - Consultar Patrimônio Total
        patrimonio = agencia.calcular_patrimonio_total()
        print(
            f"Patrimônio total da agência: R$ {patrimonio:.2f}"
        )

    elif opcao == "0":       # Opção 0 - Sair
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
        
