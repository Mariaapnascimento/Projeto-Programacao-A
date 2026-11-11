from flask import Flask, render_template, request, redirect, url_for
from models import Agencia, Banco

app = Flask(__name__)  # sem secret_key

agencia = Agencia("Agência Central", "003")
banco = Banco(agencia)


def voltar(destino, resultado, **parametros):
    """Redireciona levando a mensagem na URL."""
    sucesso, mensagem = resultado
    return redirect(url_for(
        destino,
        msg=mensagem,
        tipo="sucesso" if sucesso else "erro",
        **parametros,
    ))


@app.route("/")
def index():
    return render_template(
        "index.html",
        agencia=agencia,
        clientes=banco.clientes,
        patrimonio=agencia.calcular_patrimonio_total(),
    )


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    salario = request.form.get("salario", type=float)
    if salario is None:
        return voltar("index", (False, "Salário inválido."))
    resultado = banco.cadastrar_cliente(
        request.form["nome"], request.form["cpf"],
        salario, request.form["telefone"])
    return voltar("index", resultado)


@app.route("/contas", methods=["POST"])
def cadastrar_conta():
    numero = request.form.get("numero", type=int)
    if numero is None:
        return voltar("index", (False, "Número da conta inválido."))
    resultado = banco.cadastrar_conta(
        request.form["nome"], numero, request.form["tipo"])
    return voltar("index", resultado)


@app.route("/contas/<int:numero>")
def ver_conta(numero):
    conta = banco.procurar_conta(numero)
    if conta is None:
        return voltar("index", (False, "Conta não encontrada."))
    return render_template("conta.html", conta=conta, agencia=agencia)


@app.route("/contas/<int:numero>/<operacao>", methods=["POST"])
def operar(numero, operacao):
    conta = banco.procurar_conta(numero)
    if conta is None:
        return voltar("index", (False, "Conta não encontrada."))

    valor = request.form.get("valor", type=float)
    if valor is None:
        return voltar("ver_conta", (False, "Valor inválido."), numero=numero)

    if operacao == "depositar":
        resultado = conta.depositar(valor)
    elif operacao == "sacar":
        resultado = conta.sacar(valor)
    elif operacao == "transferir":
        destino = banco.procurar_conta(request.form.get("destino", type=int))
        if destino is None:
            resultado = (False, "Conta de destino não encontrada.")
        else:
            resultado = conta.transferir(destino, valor)
    else:
        resultado = (False, "Operação inválida.")

    return voltar("ver_conta", resultado, numero=numero)


if __name__ == "__main__":
    app.run(debug=True)