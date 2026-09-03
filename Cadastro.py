# Estruturas de dados
clientes = {}  # {cpf: nome}
contas = {}    # {numero: saldo}
titulares = {} # {numero: cpf}

# 1. CADASTRAR UM CLIENTE
print("--- 1. CADASTRAR CLIENTE ---")
cpf = input("Digite o CPF: ")
nome = input("Digite o Nome: ")
clientes[cpf] = nome
print("Cliente cadastrado!\n")

# 2. CRIAR UMA CONTA
print("--- 2. CRIAR CONTA ---")
cpf_conta = input("Digite o CPF para abrir a conta: ")
if cpf_conta in clientes:
    num_conta = "1"  # Número fixo para a conta
    contas[num_conta] = 0.0
    titulares[num_conta] = cpf_conta
    print(f"Conta {num_conta} criada com sucesso!\n")
else:
    print("CPF não encontrado.\n")

# 3. REALIZAR DEPÓSITO
print("--- 3. REALIZAR DEPÓSITO ---")
num = input("Número da conta para depósito: ")
if num in contas:
    valor = float(input("Valor do depósito: R$ "))
    contas[num] += valor
    print("Depósito realizado com sucesso!\n")

# 4. CONSULTAR SALDO
print("--- 4. CONSULTAR SALDO ---")
num = input("Número da conta para consulta: ")
if num in contas:
    cpf_dono = titulares[num]
    nome_dono = clientes[cpf_dono]
    print(f"Titular: {nome_dono} | Saldo: R$ {contas[num]:.2f}\n")

# 5. REALIZAR SAQUE
print("--- 5. REALIZAR SAQUE ---")
num = input("Número da conta para saque: ")
if num in contas:
    valor = float(input("Valor do saque: R$ "))
    if valor <= contas[num]:
        contas[num] -= valor
        print("Saque realizado com sucesso!\n")
    else:
        print("Saldo insuficiente.\n")

# CONSULTA FINAL DE CONFIRMAÇÃO
print("--- RESULTADO FINAL ---")
if "1" in contas:
    print(f"Saldo final da conta 1: R$ {contas['1']:.2f}")