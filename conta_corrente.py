# O datetime é uma biblioteca nativa do Python para manipulação de datas
from datetime import date
from conta import Conta

class ContaCorrente(Conta):

    # Função construtora. Cria um objeto ContaCorrente com os parâmetros informados (valores de atributos)
    def __init__(self, numero, titular, saldo):
        # o super() invoca funções e atributos da classe mãe
        super().__init__(numero, titular, saldo)
        # o self se refere ao objeto que foi criado e atribui à ele os valores para cada atributo
        # A lista que guardava as transações foi substituída pelo objeto historico
        #self.extrato = []
        self.historico = Historico()

    def debitar(self, quantia):
        if self.saldo > quantia:
            self.saldo -= quantia
            # adiciona a lista criada no getTransacao com as informações da transação
            # na lista de transações do historico da conta corrente
            self.historico.add_transacao(self.getTransacao('debito', quantia))
        else:
            print('Saldo insuficiente!')

    def creditar(self, quantia):
        self.saldo += quantia
        self.historico.add_transacao(self.getTransacao('credito', quantia))

    def ver_extrato_mensal(self):
        # Obtém o mês atual
        data_atual = date.today().strftime('%d/%m/%Y')
        # obter partes específicas de uma string. No caso do mês da data seriam os caracteres 4 e 5
        # Estrutura da função: string[caractere-inicial : caractere-final : pular-caractere]
        #      data 1 2 / 0 7 / 2 0 2 1
        # caractere 1 5 3 4 5 6 7 8 9 10
        mes_atual = data_atual[3:6]
        # Obtém a lista de transações do historico da conta corrente
        # e verifica uma a uma qual foi realizada no corrente mês
        for transacao in self.historico.getTransacoes():
            # O índice zero é devido a data ser o primeiro elemento da lista da transação
            data_transacao = transacao[0]
            mes_da_transacao = data_transacao[3:6]

            if mes_da_transacao == mes_atual:
                print(item)

    def getTransacao(self, operacao, quantia):
        # O date é uma classe nativa do Python para manipulação de datas
        # A função today() obtém a data do dia atual
        hoje = date.today()
        # Converte a data para o formato em texto de dd/mm/AAAA
        data_em_texto = hoje.strftime('%d/%m/%Y')

        #Se fosse necessário obter data e hora, a classe fornece a função now().
        # Ex.: data_e_hora_atual = date.now()
        # data_e_hora_em_texto = data_e_hora_atual.strftime(‘%d/%m/%Y %H:%M’)

        # Adiciona a data, operação e quantia dentro de uma lista e
        transacao = [data_em_texto, operacao, quantia]
        # E retorna a lista
        return transacao

# ==================== Classe Histórico ================== #
class Historico:
    def __init__(self):
        self.transacoes = []

    def add_transacao(self, transacao):
        self.transacoes.append(transacao)

    def getTransacoes(self):
        return self.transacoes
