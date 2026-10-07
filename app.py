from flask import Flask, render_template, request # importando ferramentas do Flask
# Flask - permite criar aplicação na web
# render_template - abre arquivos HTML
# request - pega os dados enviados pelo formulário

app = Flask(__name__)  # Cria a aplicação Flask

clientes = []          # Guarda os nomes dos clientes cadastrados
contas = []            # Guarda as contas

# Página Inicial
@app.route("/")                                           # é uma rota e a / representa a página inicial
def inicio():                                             # Cria a função que será acessada pela Rota
    return render_template("index.html")                  # Manda o index.html para o navegador

@app.route("/cadastrar-cliente", methods=["GET", "POST"]) # Cria a rota cadastrar-cliente
def cadastrar_cliente():
    if request.method == "POST":                          # o usuário enviou o formulario? se sim, execute
        nome = request.form["nome"]                       # pega o nome que veio do HTML
        clientes.append(nome)                             # Adiciona na lista
        return "Cliente cadastrado com sucesso!"          # Mostra mensagem no navegador
    return render_template("cadastrar_cliente.html")      # Só mostra o formulário

@app.route("/cadastrar-conta", methods=["GET", "POST"])   # Cria a Rota
def cadastrar_conta():
    if request.method == "POST":                          # Verifica o POST
        nome = request.form["nome"]                       # Pega o nome digitado
        numero = int(request.form["numero"])              # Pega o numero da conta
        if nome not in clientes:                          # Verifica se o cliente está na lista
            return "Cliente não encontrado."
        for conta in contas:                              # Verifica se a conta existe
            if conta["numero"] == numero:
                return "Essa conta já existe."
        nova_conta = {                                    # Cria uma nova conta, em formato de dicionário
            "numero": numero,
            "nome": nome,
            "saldo": 0                                    # começa com saldo = 0
        }
        contas.append(nova_conta)                         # adiciona a conta na lista
        return "Conta cadastrada com sucesso!"
    return render_template("cadastrar_conta.html")

@app.route("/listar-contas")                              # Rota que mostra as contas cadastradas
def listar_contas():
    return render_template(                               # Enviamos a lista contas para o HTML para ser exibida
        "listar_contas.html",
        contas=contas
    )

@app.route("/procurar-conta", methods=["GET", "POST"])    # Rota para procurar conta
def procurar_conta():
    if request.method == "POST":                          # Verifica se o formulário foi enviado
        numero = int(request.form["numero"])              # Pega o número
        for conta in contas:                              # Percorre a lista
            if conta["numero"] == numero:                 # verifica se encontrou a conta
                return render_template(                   # se sim, enviamos somente a conta encontrada para o HTML
                    "procurar_conta.html",
                    conta=conta
                )
        return "Conta não encontrada."                    # Se não for encontrada a conta
    return render_template("procurar_conta.html")

@app.route("/consultar-saldo", methods=["GET", "POST"])   # Rota para consultar-Saldo
def consultar_saldo():
    if request.method == "POST":                          # Verifica se o formulário foi enviado
        numero = int(request.form["numero"])              # Pega o número
        for conta in contas:                              # Percorre a lista
            if conta["numero"] == numero:                 # verifica se encontrou a conta
                return render_template(                   # Se sim, mostra oq encontrou
                    "consultar_saldo.html",
                    conta=conta
                )
        return "Conta não encontrada."                    # Se não
    return render_template("consultar_saldo.html")

@app.route("/depositar", methods=["GET", "POST"])         # Rota para Depositar
def depositar():
    if request.method == "POST":                          # Verifica se o formulário foi enviado
        numero = int(request.form["numero"])              # Pegamos a conta
        valor = float(request.form["valor"])              # Pegamos o valor do depósito
        for conta in contas:                              # Percorre a lista de contas
            if conta["numero"] == numero:                 # Verifica se a conta existe
                if valor > 0:                                     # Verifica se o valor do depósito é maior que zero
                    conta["saldo"] += valor                       # Adiciona o valor digitado ao Saldo
                    return "Depósito realizado com sucesso!"
                return "O valor do depósito deve ser positivo."   # Se o valor for menor que zero
        return "Conta não encontrada."                            # Se a conta não estiver na lista
    return render_template("depositar.html")

@app.route("/sacar", methods=["GET", "POST"])             # Rota para Sacar
def sacar():
    if request.method == "POST":                          # Verifica se o formulário foi enviado
        numero = int(request.form["numero"])              # Pega a conta
        valor = float(request.form["valor"])              # Pega o valor digitado
        for conta in contas:                              # Percorre a lista de contas
            if conta["numero"] == numero:                 # Verifica se a conta existe
                if valor > 0 and valor <= conta["saldo"]: # O valor de saque tem de ser maior que zero e também tem de ser menor ou igual ao valor disponivel no Saldo
                    conta["saldo"] -= valor               # Diminui o valor digitado do saldo
                    return "Saque realizado com sucesso!"
                if valor <= 0:                                     # Se o valor for menor ou igual a zero
                    return "O valor do saque deve ser positivo."
                return "Saldo insuficiente."
        return "Conta não encontrada."
    return render_template("sacar.html")

if __name__ == "__main__":        # Inicia o Flask
    app.run(debug=True)
