from conta_com_extrato import ContaBancariaComExtrato

class ContaCorrente(ContaBancariaComExtrato):

    # Função construtora. Cria um objeto ContaCorrente com os parâmetros informados (valores de atributos)
    def __init__(self, numero, titular, saldo):
        # o super() invoca funções e atributos da classe mãe
        super().__init__(numero, titular, saldo)
