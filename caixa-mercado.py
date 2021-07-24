# Escreva um programa na linguagem Python que simule o caixa de um supermercado.
# Este programa precisará ler os preços de produtos comprados, somá-los e apresentar
#o resultado ao final de cada soma.
# Após ler todos os preços de produtos, o programa deve apresentar cada um e o preço total das compras.
#
# Crie duas funções:
# Função de soma;
# Função para guardar os preço lidos;

montante = 0.0
precos = []

def soma_preco(preco):
    global montante
    montante = montante + preco

def salva_preco(preco):
    precos.append(preco)

qtde_produtos = int(input('Quantos produtos tem no carrinho?\n'))

for i in range(0, qtde_produtos):
    preco = float(input('\nInforme o preço de um produto: '))
    soma_preco(preco)
    print('\nTotal Parcial: ' + str(montante))
    salva_preco(preco)

print('\nPreços:')
for preco in precos:
    print(str(preco))

# for index in range(1, len(precos)):
#     print(str(precos[index]))

print('Total: ' + str(montante))
