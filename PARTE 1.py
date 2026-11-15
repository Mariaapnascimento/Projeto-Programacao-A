novoCliente = input("Nome do Cliente: ")
novaConta = int(input("Número da conta: "))
saldo = float(input("Saldo: R$ "))
deposito = float(input("Valor do deposito: R$ "))
saque = float(input("Valor do saque: R$ "))

if saque <= saldo:
    saldo = saldo + deposito - saque
    print("")
    print("####################################")
    print("")
    print(f" Nome: {novoCliente}\n Conta: {novaConta}\n Saldo: R$ {saldo}")
else:
    print("")
    print("####################################")
    print("")
    print("ERRO: Saldo insuficiente para realizar o saque!")
    print(f"Saldo disponivel: R$ {saldo}")
