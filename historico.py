class Historico:
    def __init__(self):
        self.transacoes = []

    def add_transacao(self, transacao):
        self.transacoes.append(transacao)

    def get_transacoes(self):
        return self.transacoes
