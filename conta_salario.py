
from conta_bancaria import ContaBancaria
class ContaSalario(ContaBancaria):

    def __init__(self, numero, titular, saldo, conta_empregador):
        super().__init__(numero, titular, saldo)
        self.empregador = conta_empregador.titular
