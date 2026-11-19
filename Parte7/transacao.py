from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo                    # identifica a operação(deposito, saque...)
        self.valor = valor                  # guarda o valor movimentado
        self.data = datetime.now()          # registra automaticamente a data e o horário
        
    def __str__(self):
        return (
            f"{self.tipo} - "
            f"R$ {self.valor:.2f} - "
            f"{self.data.strftime('%d/%m/%Y %H:%M:%S')}"
        )





