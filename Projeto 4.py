class Cliente:                      # Cria uma classe chamada Cliente
    def __init__(self, nome):       # Método construtor, executa quando um novo cliente é criado
        self.nome = nome            # Guarda o nome recebido no objeto

class Conta:                                      # Cria a Classe
    def __init__(self, numero, cliente):          # Método construtor
        self.numero = numero                      # Guarda o número da conta
        self.cliente = cliente                    # Armazena a referência ao objeto cliente
        self.saldo = 0.0                          # define o saldo inicial

    def depositar(self, valor):                      # Cria um método de deposito
        if valor > 0:                                # Verifica se o valor é maior que zero
            self.saldo += valor                      # Adiciona o valor ao saldo
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):                                # Cria o método sacar
        if valor <= 0:                                     # Verifica se o valor digitado é menor ou igual a zero
            print("O valor do saque deve ser positivo.")
        elif valor <= self.saldo:                          # Verifica se o valor digitado é menor ou igual ao saldo disponivel
            self.saldo -= valor                            # Diminui o valor do saldo
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

class Banco:                                           # Cria a classe banco, responsável por organizar os clientes e contas
    def __init__(self):                                # Inicia um objeto banco
        self.clientes = []                             # Lista para os objetos clientes
        self.contas = []                               # Lista para os objetos contas

    def cadastrar_cliente(self, nome):                 # Define o método que recebe o nome
        if self.procurar_cliente(nome) is not None:    # Verifica se o cliente já existe 
            print("Esse cliente já está cadastrado.")
            return                                     # Encerra o método

        cliente = Cliente(nome)                        # Cria um objeto da classe cliente com o nome recebido
        self.clientes.append(cliente)                  # Adiciona o objeto na lista de cliente
        print("Cliente cadastrado com sucesso!")


    def procurar_cliente(self, nome):                  # Define o método procurar cliente
        for cliente in self.clientes:                  # Percorre a lista de clientes
            if cliente.nome == nome:                   # Verifica se o nome procurado é igual ao nome do cliente
                return cliente                         # Se encontrar, retorna o objeto cliente

        return None                                    # Retorna none se não encontrar o cliente

    def cadastrar_conta(self, nome, numero):           # Define o método Cadastrar Conta
        cliente = self.procurar_cliente(nome)          # Procura o cliente informado e guarda o resultado em cliente

        if cliente is None:                            # Verifica se o cliente existe
            print("Cliente não encontrado.")
            return                                     # Encerra o método

        for conta in self.contas:                      # Percorre a lista de contas
            if conta.numero == numero:                 # Verifica se o número digitado é igual ao número de conta existente
                print("Essa conta já existe.")
                return

        conta = Conta(numero, cliente)                # Cria um objeto da classe conta, passando o número e o objeto do cliente
        self.contas.append(conta)                     # Adiciona a nova conta na lista de contas
        print("Conta cadastrada com sucesso!")

    def procurar_conta(self, numero):                 # Método Procurar Conta, recebe o númerp
        for conta in self.contas:                     # Percorre as contas
            if conta.numero == numero:                # Verifica se o número digitado existe na lista
                return conta                          # Retorna a conta encontrada

        return None                                   # Retorna none caso não encontre a conta

    def listar_clientes(self):                        # Define um método para listar clientes
        if len(self.clientes) == 0:                   # Verifica se a quantidade de elementos na lista é igual a zero
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:             # Percorre os clientes cadastrados
                print(cliente.nome)                   # Mostra o nome de cada cliente

banco = Banco()                                       # Cria um objeto da classe Banco
# A variável banco será utilizada para acessar os métodos da classe durante a execução
while True:                                           # Cria um laço de repetição que fica repetindo até uma interrupção
    print("\n##### MENU PRINCIPAL #####")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Conta")
    print("3. Lista de Contas")
    print("4. Procurar Conta")
    print("5. Consultar Saldo")
    print("6. Depositar")
    print("7. Sacar")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")             # Escolher a opção 

    if opcao == "1":                                 # opção 1 - Cadastrar Cliente
        nome = input("Digite o nome do cliente: ")   # Digita o nome
        banco.cadastrar_cliente(nome)                # Chama o método cadastrar_cliente() do objeto banco e passa o nome digitado

    elif opcao == "2":                               # Opção 2 - Cadastrar Conta
        nome = input("Digite o nome do cliente: ")
        numero = int(input("Digite o número da conta: "))
        banco.cadastrar_conta(nome, numero)          # Chama o método cadastrar_conta()

    elif opcao == "3":                               # Opção 3 - Listar contas
        if len(banco.contas) == 0:                   # Verifica se lista está vazia
            print("Nenhuma conta cadastrada.")
        else:
            print("\n### CONTAS CADASTRADAS ###")

            for conta in banco.contas:                  # Percorre todas as contas na lista
                print(f"Cliente: {conta.cliente.nome}")
                print(f"Conta: {conta.numero}")
                print(f"Saldo: R$ {conta.saldo:.2f}\n")

    elif opcao == "4":                                    # Opção 4 - Procurar Conta
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)              # Chama o método procurar_conta() e guarda o número na variável conta

        if conta is not None:                             # Verifica se a conta foi encontrata
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Conta: {conta.numero}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":                                   # Opção 5 - Consultar Saldo
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:                            # Verifica se a conta foi encontrata
            print(f"Cliente: {conta.cliente.nome}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "6":                                    # Opção 6 - Depositar
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:                              # Verifica se a conta existe
            valor = float(input("Valor do depósito: R$ ")) # digita o valor do depósito
            conta.depositar(valor)                         # Chama o método depositar() da conta
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":                                    # Opção 7 - Sacar
        numero = int(input("Digite o número da conta: "))
        conta = banco.procurar_conta(numero)

        if conta is not None:                             # Verifica se a conta existe
            valor = float(input("Valor do saque: R$ "))
            conta.sacar(valor)                            # Chama o método
            print(f"Saldo atual: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "0":                                    # Opção 0 - Sair
        print("Programa encerrado.")
        break                                             # Encerra o laço

    else:                                                 # Caso o usuário escolha qualquer outra opção
        print("Opção inválida.")

