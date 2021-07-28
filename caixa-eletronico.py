from conta_corrente import ContaCorrente
from conta_salario import ContaSalario
from conta_poupanca import ContaPoupanca
from datetime import date, timedelta

print('Criando contas...')
conta1 = ContaCorrente('123-4', 'Mano', 100)
conta2 = ContaCorrente('432-1', 'Valter', 200)
conta3 = ContaSalario('123-1', 'Zé', 300, conta2)
conta4 = ContaPoupanca('3232-2', 'Bastião', 500)
print('Contas criadas!')

print('======Transferindo de Mano para Valter=====')
conta1.transferir(conta2, 50)

print('======Depositando na conta de Mano=====')
conta1.depositar(50)

print('======Valter pagando o salário de Zé=====')
conta2.transferir(conta3, 150)

conta3.ver_saldo()

print('======Verificando rendimento da poupança de Bastião com 29 dias=====')
conta4.render(date.today() + timedelta(days=29))

print('======Verificando rendimento da poupança de Bastião com 30 dias=====')
conta4.render(date.today() + timedelta(days=30))
conta4.ver_saldo()
