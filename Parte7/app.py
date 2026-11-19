from flask import Flask, render_template, request, redirect, url_for  
from agencia import Agencia
from banco import Banco
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
import os
from persistencia import (
    salvar_dados_bancarios,
    carregar_dados_bancarios
)
from graficos import (
    grafico_patrimonio_cliente,
    grafico_movimentacoes_mensais,
    grafico_evolucao_cliente,
    grafico_media_salarial,
    grafico_evolucao_saldo,
    grafico_evolucao_saldo_conta
)

app = Flask(__name__)

if os.path.exists("dados_bancarios.json"):          # verifica se o arquivo existe
    banco = carregar_dados_bancarios()              # recupera os dados salvos
    agencia = banco.agencia                         # recupera a agencia do banco
else:
    agencia = Agencia("Agência Central", "003")
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
        salvar_dados_bancarios(banco)
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
        taxaManutencao = float(request.form.get("taxaManutencao", 0))
        taxaRendimento = float(request.form.get("taxaRendimento", 0))
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
        banco.cadastrar_conta(nome, numero, tipo, taxaManutencao, taxaRendimento)   # Cadastra a conta
        salvar_dados_bancarios(banco)
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
        grafico = None
        if conta is not None:
            grafico = grafico_evolucao_saldo_conta(conta)
        if conta is None:
            return render_template(
                "consultar_saldo.html",
                conta=None,
                mensagem="Conta não encontrada."
            )
        return render_template(
            "consultar_saldo.html",
            conta=conta,
            grafico=grafico
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
            salvar_dados_bancarios(banco)
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
            salvar_dados_bancarios(banco)
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
                salvar_dados_bancarios(banco)
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

@app.route("/descontar-taxa", methods=["GET", "POST"])
def descontar_taxa():
    mensagem = ""
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            mensagem = "Conta não encontrada."
        elif not isinstance(conta, ContaCorrente):
            mensagem = "Esta operação é exclusiva para conta corrente."
        elif conta.DescontarTaxa():
            salvar_dados_bancarios(banco)
            mensagem = "Taxa descontada com sucesso!"
        else:
            mensagem = "Não foi possível descontar a taxa."
    return render_template("descontar_taxa.html", mensagem=mensagem)

@app.route("/aplicar-rendimento", methods=["GET", "POST"])
def aplicar_rendimento():
    mensagem = ""
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            mensagem = "Conta não encontrada."
        elif not isinstance(conta, ContaPoupanca):
            mensagem = "Esta operação é exclusiva para conta poupança."
        elif conta.AplicarRendimento():
            salvar_dados_bancarios(banco)
            mensagem = "Rendimento aplicado com sucesso!"
        else:
            mensagem = "Não foi possível aplicar o rendimento."
    return render_template("aplicar_rendimento.html", mensagem=mensagem)

@app.route("/historico-saldo", methods=["GET", "POST"])
def historico_saldo():
    historico = []
    mensagem = ""
    if request.method == "POST":
        numero = int(request.form["numero"])
        conta = banco.procurar_conta(numero)
        if conta is None:
            mensagem = "Conta não encontrada."
        else:
            historico = conta.exibirHistoricoSaldo()
    return render_template(
        "historico_saldo.html",
        historico=historico,
        mensagem=mensagem
    )
    

@app.route("/graficos")
def exibir_graficos():
    grafico_barras = grafico_media_salarial(agencia)
    grafico_linhas = grafico_evolucao_saldo(agencia)

    return render_template(
        "graficos.html",
        grafico_barras=grafico_barras,
        grafico_linhas=grafico_linhas
    )

@app.route("/patrimonio/<cpf>")
def exibir_patrimonio(cpf):
    cliente = None

    for c in banco.clientes:
        if c.cpf == cpf:
            cliente = c
            break

    if cliente is None:
        return render_template(
            "selecionar_cliente.html",
            erro="Cliente não encontrado. Verifique o CPF e tente novamente."
        )

    grafico_pizza = grafico_patrimonio_cliente(agencia, cliente)
    grafico_barras = grafico_movimentacoes_mensais(agencia, cliente)
    grafico_linhas = grafico_evolucao_cliente(agencia, cliente)

    return render_template(
        "patrimonio_cliente.html",
        cliente=cliente,
        grafico_pizza=grafico_pizza,
        grafico_barras=grafico_barras,
        grafico_linhas=grafico_linhas
    )
@app.route("/selecionar-cliente", methods=["GET", "POST"])
def selecionar_cliente():
    if request.method == "POST":
        cpf = request.form["cpf"]
        return redirect(
            url_for("exibir_patrimonio", cpf=cpf)
        )
    return render_template("selecionar_cliente.html")


if __name__ == "__main__":
    app.run(debug=True)
