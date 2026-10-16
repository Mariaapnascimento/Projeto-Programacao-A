class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome):
        if self.procurar_cliente(nome) is not None:
            print("Esse cliente já está cadastrado.")
            return

        cliente = Cliente(nome)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")


    def procurar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente

        return None

    def cadastrar_conta(self, nome, numero):
        cliente = self.procurar_cliente(nome)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        for conta in self.contas:
            if conta.numero == numero:
                print("Essa conta já existe.")
                return

        conta = Conta(numero, cliente)
        self.contas.append(conta)
        print("Conta cadastrada com sucesso!")

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta

        return None

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(cliente.nome)

banco = Banco()

while True:
    print("\n##### MENU PRINCIPAL #####")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Conta")
    print("3. Lista de Contas")
    print("4. Procurar Conta")
    print("5. Consultar Saldo")
    print("6. Depositar")
    print("7. Sacar")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        banco.cadastrar_cliente(nome)

    elif opcao == "2":
        nome = input("Digite o nome do cliente: ")
        numero = int(input("Digite o número da conta: "))
        banco.cadastrar_conta(nome, numero)

    elif opcao == "3":
        if len(banco.contas) == 0:
            print("Nenhuma conta cadastrada.")
        else:
            print("\n### CONTAS CADASTRADAS ###")

            for conta in banco.contas:
                print(f"Cliente: {conta.cliente.nome}")
                print(f"Conta: {conta.numero}")
                print(f"Saldo: R$ {conta.saldo:.2f}\n")

    elif opcao == "4":
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Conta: {conta.numero}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "6":
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:
            valor = float(input("Valor do depósito: R$ "))
            conta.depositar(valor)
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:
            valor = float(input("Valor do saque: R$ "))
            conta.sacar(valor)
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
