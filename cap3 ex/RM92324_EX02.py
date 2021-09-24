# recebe:
# Quantidade de transações
# Informar o valor de cada uma
# exibir:
# Valor total de gastos e a média de cada transação

quantidade_transacoes   = int(input("Por favor, digite a quantidade de transações: "))
total_transacao         = 0

for i in range(0, quantidade_transacoes):
    valor_da_transacao   = float(input("Informe o valor da {}° transação: ".format(i+1)))
    total_transacao     += valor_da_transacao
print("Total de transações é:  {:.2f}".format(total_transacao))
print("A média cada transação é: {:.2f}".format(total_transacao / quantidade_transacoes))