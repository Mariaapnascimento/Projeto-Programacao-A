import json
from cliente import Cliente
from agencia import Agencia
from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from transacao import Transacao
from datetime import datetime
from banco import Banco


def salvar_dados_bancarios(banco, nome_arquivo="dados_bancarios.json"):  # Recebe o objeto da classe Banco (Clientes e agencia)
    dados_export = []                                                    # Guarda os dados
    agencia = banco.agencia                                              # acessa a agencia

    agencia_dict = {                                                     # Cria um dicionario
        "nome": agencia.nome,
        "numero": agencia.numero,
        "clientes": []
    }

    for cliente in banco.clientes:                                      # Percorre a lista de clientes
        cliente_dict = {                                                # Cria um dicionario
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "salario": cliente.salario,
            "telefone": cliente.telefone,
            "contas": []
        }

        for conta in agencia.contas:                                    # percorre a lista de contas da agencia
            if conta.cliente is cliente:                                # verificamos se a conta pertence ao cliente
                conta_dict = {                                          # cria um dicionario
                    "numero": conta.numero,
                    "tipo": conta.tipo,
                    "saldo": conta.saldo,
                    "historico_saldos": conta.historico_saldos,
                    "transacoes": [],
                    "ultimo_desconto": (                                # guarda a data da última manutenção
                        conta.ultimo_desconto.isoformat()               # transforma a data em texto para que possa ser armazenada no JSON
                        if isinstance(conta, ContaCorrente) and conta.ultimo_desconto
                        else None
                    ),
                    "ultimo_rendimento": (                              # guarda a data da último rendimento
                        conta.ultimo_rendimento.isoformat()             # transforma a data em texto para que possa ser armazenada no JSON
                        if isinstance(conta, ContaPoupanca) and conta.ultimo_rendimento
                        else None
                    )
                }

                if isinstance(conta, ContaCorrente):                     # verifica o tipo da conta
                    conta_dict["taxaManutencao"] = conta.taxaManutencao  # adicionamos ao dicionário a taxa
                elif isinstance(conta, ContaPoupanca):                   # verifica o tipo da conta
                    conta_dict["taxaRendimento"] = conta.taxaRendimento  # adicionamos ao dicionário a taxa

                for transacao in conta.historico_transacoes:             # percorre o historico de transação
                    transacao_dict = {                                   # cria um dicionario
                        "tipo": transacao.tipo,
                        "valor": transacao.valor,
                        "data": transacao.data.isoformat()
                    }

                    conta_dict["transacoes"].append(transacao_dict)      # adiciona a transação ao dicionario conta
                cliente_dict["contas"].append(conta_dict)                # adiciona a conta ao dicionario cliente
        agencia_dict["clientes"].append(cliente_dict)                    # adiciona o cliente ao dicionario agencia
    dados_export.append(agencia_dict)                                    # adiciona o dicionario da agencia a lista principal
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:           # Salva o arquivo json
        json.dump(dados_export, arquivo, indent=4, ensure_ascii=False)   # transforma os dados da lista em JSON e grava no arquivo
    print(f"Dados salvos com sucesso em {nome_arquivo}!")

def carregar_dados_bancarios(nome_arquivo="dados_bancarios.json"):       # função para recuperar os dados armazenados
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:           # abre o arquivo json
        dados_brutos = json.load(arquivo)                                # le o json e transforma os dados em estruturas python
    dados_agencia = dados_brutos[0]                                      # recupera os dados da agencia

    agencia = Agencia(                                                   # # cria um novo objeto da classe agencia
        dados_agencia["nome"],
        dados_agencia["numero"]
    )

    banco = Banco(agencia)                                              # cria um novo objeto da classe banco
    for dados_cliente in dados_agencia["clientes"]:                     # percorre a lista de clientes armazenadas no json
        cliente = Cliente(                                              # cria um novo objeto da classe cliente
            dados_cliente["nome"],
            dados_cliente["cpf"],
            dados_cliente["salario"],
            dados_cliente["telefone"]
        )

        banco.clientes.append(cliente)                                  # adiciona cliente na lista dos clientes do banco
        for dados_conta in dados_cliente["contas"]:                     # percorre as contas
            if dados_conta["tipo"] == "Corrente":
                conta = ContaCorrente(
                dados_conta["numero"],
                cliente
        )
            elif dados_conta["tipo"] == "Poupança":
                conta = ContaPoupanca(
                dados_conta["numero"],
                cliente
        )
            else:
                continue

            conta.saldo = dados_conta["saldo"]
            conta.historico_saldos = dados_conta["historico_saldos"]

            if isinstance(conta, ContaCorrente):
                data_desconto = dados_conta.get("ultimo_desconto")
                if data_desconto:
                    conta.ultimo_desconto = datetime.fromisoformat(data_desconto)
            elif isinstance(conta, ContaPoupanca):
                data_rendimento = dados_conta.get("ultimo_rendimento")
                if data_rendimento:
                    conta.ultimo_rendimento = datetime.fromisoformat(data_rendimento)
            for dados_transacao in dados_conta["transacoes"]:           # percorre todas as transações da conta
                transacao = Transacao(                                  # cria um novo objeto da classe transação
                    dados_transacao["tipo"],
                    dados_transacao["valor"]
                )
                transacao.data = datetime.fromisoformat(
                    dados_transacao["data"]
                )
                conta.historico_transacoes.append(transacao)           # adiciona o objeto transação ao historico
                
            if isinstance(conta, ContaCorrente) and conta.ultimo_desconto is None:
                for transacao in reversed(conta.historico_transacoes):   # percorre o histórico começando pela transação mais recente
                    if transacao.tipo == "TAXA_MANUTENCAO":
                        conta.ultimo_desconto = transacao.data
                        break
            elif isinstance(conta, ContaPoupanca) and conta.ultimo_rendimento is None:
                for transacao in reversed(conta.historico_transacoes):   # percorre o histórico começando pela transação mais recente
                    if transacao.tipo == "RENDIMENTO":
                        conta.ultimo_rendimento = transacao.data
                        break
            agencia.contas.append(conta)                               # adiciona a conta na lista de contas da agencia

    print("Dados bancários carregados com sucesso!")
    return banco



