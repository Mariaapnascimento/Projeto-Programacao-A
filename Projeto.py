nomes = []
contas = []
saldos = []

while True:
    print("\n##### MENU PRINCIPAL #####\n")
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
        nomes.append(nome)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do cliente: ")
        if nome in nomes:
            conta = int(input("Digite o número da conta: "))
            if conta not in contas:
                contas.append(conta)
                saldos.append(0)
                print("Conta cadastrada com sucesso!")
            else:
                print("Essa conta já existe.")
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        if len(contas) == 0:
            print("Nenhuma conta cadastrada.")
        else:
            print("\n### CONTAS CADASTRADAS ###")
            for i in range(len(contas)):
                print(f"Cliente: {nomes[i]}")
                print(f"Conta: {contas[i]}")
                print(f"Saldo: R$ {saldos[i]:.2f}\n")

    elif opcao == "4":
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            print(f"Cliente: {nomes[posicao]}")
            print(f"Conta: {contas[posicao]}")
            print(f"Saldo: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            print(f"Cliente: {nomes[posicao]}")
            print(f"Saldo: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "6":
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            deposito = float(input("Valor do depósito: R$ "))
            if deposito > 0:
                saldos[posicao] = saldos[posicao] + deposito
                print("Depósito realizado com sucesso!")
                print(f"Saldo atual: R$ {saldos[posicao]:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            saque = float(input("Valor do saque: R$ "))
            if saque <= saldos[posicao]:
                saldos[posicao] = saldos[posicao] - saque
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldos[posicao]:.2f}")
            else:
                print(f"Saldo insuficiente! Saldo atual: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

