import plotly.express as px                         # importa a biblioteca


def grafico_patrimonio_cliente(agencia, cliente):
    contas_cliente = []
    for conta in agencia.contas:
        if conta.cliente.cpf == cliente.cpf:
            contas_cliente.append(conta)
    nomes_contas = []
    saldos = []
    for conta in contas_cliente:
        nomes_contas.append(
            f"Conta {conta.numero} - {conta.tipo}"
        )
        saldos.append(conta.saldo)
    figura = px.pie(
        names=nomes_contas,
        values=saldos,
        title=f"Distribuição do Patrimônio de {cliente.nome}"
    )
    figura.update_layout(
        height=350,
        autosize=True
    )
    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )

def grafico_movimentacoes_mensais(agencia, cliente):
    movimentacoes = {}
    for conta in agencia.contas:
        if conta.cliente.cpf == cliente.cpf:
            for transacao in conta.historico_transacoes:
                if transacao.tipo == "DEPOSITO" or transacao.tipo == "SAQUE":
                    ano = transacao.data.year
                    mes = transacao.data.month
                    tipo = transacao.tipo
                    chave = (ano, mes, tipo)
                    if chave not in movimentacoes:
                        movimentacoes[chave] = 0
                    movimentacoes[chave] += transacao.valor
    if not movimentacoes:
        return "<p>Não há depósitos ou saques registrados.</p>"

    dados = []

    for chave in sorted(movimentacoes):
        ano, mes, tipo = chave

        dados.append({
            "Mês": f"{mes:02d}/{ano}",
            "Tipo": tipo,
            "Valor": movimentacoes[chave]
        })

    figura = px.bar(
        dados,
        x="Mês",
        y="Valor",
        color="Tipo",
        barmode="group",
        title=f"Depósitos e Saques Mensais - {cliente.nome}",
        labels={
            "Mês": "Mês/Ano",
            "Valor": "Valor (R$)",
            "Tipo": "Tipo de Operação"
        }
    )

    figura.update_layout(
        height=350,
        autosize=True
    )

    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )
def grafico_evolucao_cliente(agencia, cliente):
    dados = []
    for conta in agencia.contas:
        if conta.cliente.cpf == cliente.cpf:
            for i, transacao in enumerate(conta.historico_transacoes):
                dados.append({
                    "Data": transacao.data,
                    "Saldo": conta.historico_saldos[i + 1],
                    "Conta": str(conta.numero),
                    "Operação": transacao.tipo,
                    "Valor movimentado": transacao.valor
                })

    if not dados:
        return "<p>Não há transações registradas para este cliente.</p>"
    figura = px.line(
        dados,
        x="Data",
        y="Saldo",
        color="Conta",
        markers=True,
        hover_data=["Operação", "Valor movimentado"],
        title=f"Evolução do Saldo e das Transações - {cliente.nome}",
        labels={
            "Data": "Data da Operação",
            "Saldo": "Saldo (R$)",
            "Conta": "Número da Conta",
            "Operação": "Tipo de Operação",
            "Valor movimentado": "Valor (R$)"
        }
    )
    figura.update_layout(
        height=350,
        autosize=True
    )
    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )
def grafico_media_salarial(agencia):
    clientes_por_tipo = {
        "Corrente": {},
        "Poupança": {}
    }
    for conta in agencia.contas:
        tipo = conta.tipo
        cpf = conta.cliente.cpf
        salario = float(conta.cliente.salario)
        clientes_por_tipo[tipo][cpf] = salario
        
    tipos = ["Corrente", "Poupança"]
    medias = []
    for tipo in tipos:
        salarios = list(clientes_por_tipo[tipo].values())
        if len(salarios) > 0:
            media = sum(salarios) / len(salarios)
        else:
            media = 0
        medias.append(media)
        
    figura = px.bar(
        x=tipos,
        y=medias,
        title="Média Salarial por Tipo de Conta",
        labels={
            "x": "Tipo de Conta",
            "y": "Média Salarial (R$)"
        }
    )
    figura.update_layout(
        height=350,
        autosize=True
    )
    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )
    

def grafico_evolucao_saldo(agencia):
    dados = []
    for conta in agencia.contas:
        for i, saldo in enumerate(conta.historico_saldos):
            dados.append({
                "Conta": str(conta.numero),
                "Operação": i,
                "Saldo": saldo
            })

    figura = px.line(
        dados,
        x="Operação",
        y="Saldo",
        color="Conta",
        title="Evolução do Saldo das Contas",
        markers=True
    )

    figura.update_layout(
        height=350,
        autosize=True
    )
    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )

def grafico_evolucao_saldo_conta(conta):
    dados = []
    for i, saldo in enumerate(conta.historico_saldos):
        dados.append({
            "Operação": i,
            "Saldo": saldo
        })
    figura = px.line(
        dados,
        x="Operação",
        y="Saldo",
        title=f"Evolução do Saldo da Conta {conta.numero}",
        markers=True
    )
    figura.update_layout(height=350, autosize=True)
    return figura.to_html(
        full_html=False,
        config={"responsive": True}
    )

