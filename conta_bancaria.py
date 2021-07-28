# 1. Usar composição para guardar o histórico de transações (classe Historico)
#   Quando usar composição?
#   Basta observar duas palavras: tem um. Ex.: Uma conta corrente tem um histórico
#   transações
# 2. Usar Herança e dividir uma conta corrente de uma conta salário

class ContaBancaria:

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def sacar(self, quantia):
        self.debitar(quantia)
        self.ver_saldo()

    def depositar(self, quantia):
        self.creditar(quantia)
        self.ver_saldo()

    def ver_saldo(self):
        print('titular: '+ self.titular +'\nSaldo da conta: ' + str(self.saldo))

    def debitar(self, quantia):
        if self.saldo > quantia:
            self.saldo -= quantia
        else:
            print('Saldo insuficiente!')

    def creditar(self, quantia):
        self.saldo += quantia

    def transferir(self, destinatario, quantia):
        # Verifica se ele é um empregador e está transferindo para uma conta salário
        # Se for retornado True, ele é empregador, se for retornado False, não é empregador
        # e a conta é uma conta corrente
        if self.isEmpregador(destinatario) or hasattr(destinatario, 'historico'):
            destinatario.depositar(quantia)
            self.debitar(quantia)
            print('Transferência de R$ '+ str(quantia) +' realizada para '+ destinatario.titular)
            self.ver_saldo()
        else:
            print('Você não pode transferir para uma conta salário. Ou a conta de destino não é conta corrente!')

    # Verifica se a conta de destino da transferência é conta salários
    # e se o titular da conta que está fazendo a transferência é um empregador
    def isEmpregador(self, conta):
        if hasattr(conta, 'empregador') and self.titular is conta.empregador:
            return True
        else:
            return False
