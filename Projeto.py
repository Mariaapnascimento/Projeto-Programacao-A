nomes = []      #lista para guardar os nomes
contas = []     #guardar contas
saldos = []     #guardar saldos

while True:     # para o menu continuar aparecendo
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

    if opcao == "1":                                  #cadastro de cliente
        nome = input("Digite o nome do cliente: ")    #Digitar nome do cliente
        nomes.append(nome)                            #adiciona o nome na lista 
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":                                         #Cadastro de conta
        nome = input("Digite o nome do cliente: ")             #Digitar o nome do cliente
        if nome in nomes:                                      #Verifica se o nome está na lista
            conta = int(input("Digite o número da conta: "))   #Digite a conta
            if conta not in contas:                            #verifica se a conta está na lista
                contas.append(conta)                           #se não estiver adiciona a conta na lista
                saldos.append(0)                               #adiciona um saldo inicial na lista
                print("Conta cadastrada com sucesso!")
            else:
                print("Essa conta já existe.")
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":                                      #listar contas
        if len(contas) == 0:                                #verifica se a quantidade de elementos dentro da lista
            print("Nenhuma conta cadastrada.")              # se len = 0
        else:
            print("\n### CONTAS CADASTRADAS ###")
            for i in range(len(contas)):                    #percorre os elementos da lista 
                print(f"Cliente: {nomes[i]}")
                print(f"Conta: {contas[i]}")
                print(f"Saldo: R$ {saldos[i]:.2f}\n")

    elif opcao == "4":                                      #Procurar conta
        procurar = int(input("Digite o número da conta: ")) #Digitar o número da conta
        if procurar in contas:                              #Verifica se o número digitado está na lista
            posicao = contas.index(procurar)                #verifica a posição da conta
            print(f"Cliente: {nomes[posicao]}")
            print(f"Conta: {contas[posicao]}")
            print(f"Saldo: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "5":                                      #Consultar Saldo
        procurar = int(input("Digite o número da conta: ")) #Digitar o número da conta
        if procurar in contas:                              #verifica se a conta está na lista
            posicao = contas.index(procurar)                #Verifica a posição
            print(f"Cliente: {nomes[posicao]}")
            print(f"Saldo: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "6":                                        #Fazer Depósito
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            deposito = float(input("Valor do depósito: R$ "))  #Digitar o valor do depósito
            if deposito > 0:                                   #Verifica se o valor é maior que zero
                saldos[posicao] = saldos[posicao] + deposito   #Se sim, atualiza o saldo
                print("Depósito realizado com sucesso!")
                print(f"Saldo atual: R$ {saldos[posicao]:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":                                         #Fazer Saque
        procurar = int(input("Digite o número da conta: "))
        if procurar in contas:
            posicao = contas.index(procurar)
            saque = float(input("Valor do saque: R$ "))        #Digitar o valor do saque
            if saque <= saldos[posicao]:                       #Verifica se o valor do saque é menor ou igual ao saldo da conta
                saldos[posicao] = saldos[posicao] - saque      #Se sim, atualiza o saldo retirando o valor do saque
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldos[posicao]:.2f}")
            else:
                print(f"Saldo insuficiente! Saldo atual: R$ {saldos[posicao]:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao == "0":                         #Voltar
        print("Programa encerrado.")
        break                                  #sai do while
    else:
        print("Opção inválida.")               #Qualquer outra opção que não está no MENU


