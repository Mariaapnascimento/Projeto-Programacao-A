from flask import Flask, render_template, request
from agencia import Agencia
from banco import Banco

app = Flask(__name__)
agencia = Agencia("Agência Central", "003")  # Criação dos objetos principais
banco = Banco(agencia)

@app.route("/")  # Página inicial
def inicio():
    return render_template("index.html")

@app.route("/cadastrar-cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        nome = request.form["nome"]             #recebe o nome digitado
        cpf = request.form["cpf"]
        salario = float(request.form["salario"])
        telefone = request.form["telefone"]
        if banco.procurar_cliente(nome) is not None:  #verifica se já existe um cliente com esse nome
            return "Esse cliente já está cadastrado."
        banco.cadastrar_cliente(nome, cpf, salario, telefone)   #chama o método da classe banco e cria o objeto cliente
        return render_template(
            "cadastrar_cliente.html",
            mensagem="Cliente cadastrado com sucesso!"
                )
    return render_template("cadastrar_cliente.html")

@app.route("/cadastrar-conta", methods=["GET", "POST"])
def cadastrar_conta():
    if request.method == "POST":
        nome = request.form["nome"]
        numero = int(request.form["numero"])
        tipo = request.form["tipo"]
        if banco.procurar_cliente(nome) is None:   # Verifica se o cliente está cadastrado
            return render_template(
                "cadastrar_conta.html",
                mensagem="Cliente não encontrado."
            )
        if banco.procurar_conta(numero) is not None:  # Verifica se o número da conta já existe
            return render_template(
                "cadastrar_conta.html",
                mensagem="Essa conta já está cadastrada."
            )
        banco.cadastrar_conta(nome, numero, tipo)   # Cadastra a conta
        return render_template(
            "cadastrar_conta.html",
            mensagem="Conta cadastrada com sucesso!"
        )
    return render_template("cadastrar_conta.html")

@app.route("/listar-contas")
def listar_contas():
    contas = banco.agencia.contas

    return render_template(
        "listar_contas.html",
        contas=contas
    )
    
@app.route("/procurar-conta", methods=["GET", "POST"])
def procurar_conta():
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            return render_template(
                "procurar_conta.html",
                conta=None,
                mensagem="Conta não encontrada."
            )
        return render_template(
            "procurar_conta.html",
            conta=conta
        )
    return render_template(
        "procurar_conta.html",
        conta=None
    )
    
@app.route("/consultar-saldo", methods=["GET", "POST"])
def consultar_saldo():
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            return render_template(
                "consultar_saldo.html",
                conta=None,
                mensagem="Conta não encontrada."
            )
        return render_template(
            "consultar_saldo.html",
            conta=conta
        )
    return render_template(
        "consultar_saldo.html",
        conta=None
    )

@app.route("/depositar", methods=["GET", "POST"])
def depositar():
    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])
        conta = banco.procurar_conta(numero)    # Procura a conta
        if conta is None:
            return render_template(
                "depositar.html",
                mensagem="Conta não encontrada."
            )
        resultado = conta.depositar(valor)   # Realiza o depósito
        if resultado:
            mensagem = "Depósito realizado com sucesso!"
        else:
            mensagem = "O valor do depósito deve ser positivo."
        return render_template(
            "depositar.html",
            mensagem=mensagem
        )
    return render_template("depositar.html")

@app.route("/sacar", methods=["GET", "POST"])
def sacar():
    if request.method == "POST":
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])
        conta = banco.procurar_conta(numero)  # Procura a conta
        if conta is None:
            return render_template(
                "sacar.html",
                mensagem="Conta não encontrada."
            )
        resultado = conta.sacar(valor)   # Realiza o saque
        if resultado:
            mensagem = "Saque realizado com sucesso!"
        elif valor <= 0:
            mensagem = "O valor do saque deve ser positivo."
        else:
            mensagem = "Saldo insuficiente."
        return render_template(
            "sacar.html",
            mensagem=mensagem
        )
    return render_template("sacar.html")

@app.route("/transferir", methods=["GET", "POST"])
def transferir():
    if request.method == "POST":
        numero_origem = int(request.form["numero_origem"])
        numero_destino = int(request.form["numero_destino"])
        valor = float(request.form["valor"])
        conta_origem = banco.procurar_conta(numero_origem)
        conta_destino = banco.procurar_conta(numero_destino)
        if conta_origem is None:
            mensagem = "Conta de origem não encontrada."
        elif conta_destino is None:
            mensagem = "Conta de destino não encontrada."
        else:
            resultado = conta_origem.transferir(        # Realiza a transferência
                conta_destino, valor
            )
            if resultado == "sucesso":
                mensagem = "Transferência realizada com sucesso!"
            elif resultado == "valor_invalido":
                mensagem = "O valor da transferência deve ser positivo."
            elif resultado == "mesma_conta":
                mensagem = "Não é possível transferir para a mesma conta."
            elif resultado == "saldo_insuficiente":
                mensagem = "Saldo insuficiente."
        return render_template(
            "transferir.html",
            mensagem=mensagem
        )
    return render_template("transferir.html")

@app.route("/historico", methods=["GET", "POST"])
def historico():
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            return render_template(
                "historico.html",
                conta=None,
                transacoes=None,
                mensagem="Conta não encontrada."
            )
        transacoes = conta.mostrar_historico()
        return render_template(
            "historico.html",
            conta=conta,
            transacoes=transacoes
        )
    return render_template(
        "historico.html",
        conta=None,
        transacoes=None
    )
    
@app.route("/patrimonio")
def patrimonio():
    total = agencia.calcular_patrimonio_total()
    return render_template(
        "patrimonio.html",
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)
