from cliente import Cliente
from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

class Banco:
    # Classe responsável pelo cadastro e pela busca de clientes
    # e pela comunicação com a agência
    def __init__(self, agencia):
        self.clientes = []
        self.agencia = agencia

    def cadastrar_cliente(self, nome, cpf, salario, telefone):
        if self.procurar_cliente(nome) is not None:
            print("Esse cliente já está cadastrado.")
            return
        cliente = Cliente(nome, cpf, salario, telefone)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def procurar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        return None

    def cadastrar_conta(self, nome, numero, tipo, taxaManutencao=0.0, taxaRendimento=0.0):
        cliente = self.procurar_cliente(nome)
        if cliente is None:
            print("Cliente não encontrado.")
            return
        if tipo == "Corrente":
            conta = ContaCorrente(numero, cliente, taxaManutencao)
        elif tipo == "Poupança":
            conta = ContaPoupanca(numero, cliente, taxaRendimento)
        else:
            print("Tipo de conta inválido.")
            return
        self.agencia.adicionar_conta(conta)

    def procurar_conta(self, numero):
        return self.agencia.buscar_conta(numero)

    def listar_contas(self):
        self.agencia.listar_contas()


