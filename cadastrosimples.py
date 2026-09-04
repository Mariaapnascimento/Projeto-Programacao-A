#BANCO/projeto mais simples, sem funções, sem dicionários, apenas para fins de estudo
print ("--- BANCO ---")
print ("1. CADASTRAR CLIENTE") 
if input('Você deseja se cadastrar? (s/n)')== 's':
    cpf = input("Digite o CPF: ")
    nome= input("Digite o Nome: ")
    print ('cliente' , nome, 'cadastrado com sucesso!')
    if input('Você já possui cadastro? (s/n)')== 'n':
        print("Cadastro de cliente")
        cpf = input("Digite o CPF: ")
        nome =  input("Digite o Nome: ")
        print ('cliente' , nome, 'cadastrado com sucesso!')
    else:
        print ("Você já possui cadastro, não é necessário se cadastrar novamente.")   
        cpf = input("Digite o CPF: ") 
else: 
    print  ("Você não se cadastrou, você precisa se cadastrar para abrir uma conta.")

#2 PARTE PARA CRIAR A CONTA
print ("2. CRIAR CONTA")
if cpf == input("Digite o CPF para abrir a conta: "):
    conta = cpf + "2026" # Número da conta quando for criada
    print ("Sua conta é o seu cpf mais 2026, ou seja, sua conta é: ", conta)
    print(f"Conta {conta} criada com sucesso!\n")
else:
    print ("CPF não encontrado, você precisa se cadastrar primeiro.")

#3 PARTE PARA REALIZAR O DEPÓSITO
print ("3. REALIZAR DEPÓSITO")
if conta == input("Número da sua conta para depósito: "):
    valor = float(input("Valor do depósito: R$ "))
    print ("Depósito realizado com sucesso!\n")
else:
    print ("Conta não encontrada, você precisa criar uma conta primeiro.")

#4 PARTE PARA CONSULTAR O SALDO
print ("4. CONSULTAR SALDO")
if conta == input("Número da conta para consulta: "):
    print ("Titular: ", nome, " / Saldo: R$ ", valor)
else:
    print ("Conta não encontrada, você precisa criar uma conta primeiro.")

#5 PARTE PARA REALIZAR O SAQUE
print ("5. REALIZAR SAQUE")
if conta == input("Número da conta para saque: "):
    saque = float(input("Valor do saque: R$ "))
    if saque <= valor: #saque precisa ser menor ou igual ao valor do saldo
        valor -= saque #o valor do saldo é menos o valor do saque (valor = valor - saque)
        print ("Saque realizado com sucesso!\n")
    else:
        print ("Saldo insuficiente.\n")
else:
    print ("Conta não encontrada, você precisa criar uma conta primeiro.")

#Consulta do saldo final
print ("--- RESULTADO FINAL ---")
if conta == input("Número da conta para consulta: "):
    print ("Titular: ", nome, " / Saldo final: R$ ", valor)
else:
    print ("Conta não encontrada, voce precisa consultar contas existentes.")            