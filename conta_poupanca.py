from conta_com_extrato import ContaBancariaComExtrato
from datetime import date, timedelta

class ContaPoupanca(ContaBancariaComExtrato):

    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.menor_quantia = self.saldo
        self.contador_dias = 0
        self.selic = 4.32
        self.data_aniver_deposito = date.today()
        # Quando inicializa uma conta poupança, já fica configurada a próxima
        # data de rendimento, a qual é atualizada sempre que a data for alcançada
        self.data_prox_rendimento = self.data_aniver_deposito + timedelta(days=30)

    def render(self, data_atual):
        # Se a data atual é após ou no dia do próximo rendimento
        if(data_atual >= self.data_prox_rendimento):
            self.saldo += ((self.menor_quantia * self.selic)/100)
            self.atualizar_data_prox_rendimento()
            self.atualizar_menor_valor()
        else:
            print('Ainda não completou 30 dias para calcular o rendimento!')

    def debitar(self, quantia):
        if self.saldo > quantia:
            self.saldo -= quantia
            if self.saldo < self.menor_quantia:
                self.atualizar_menor_valor()
            if hasattr(self, 'historico'):
                # adiciona a lista criada no getTransacao com as informações da transação
                # na lista de transações do historico da conta corrente
                self.historico.add_transacao(self.montar_transacao('debito', quantia))
        else:
            print('Saldo insuficiente!')

    def atualizar_menor_valor(self):
        self.menor_quantia = self.saldo

    def atualizar_data_prox_rendimento(self):
        nova_data = self.data_prox_rendimento + timedelta(days=30)
        self.data_prox_rendimento = nova_data
