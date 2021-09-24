# RECEBE: TIPO DE ASSINATURA, FATURAMENTO ANUAL
# CALCULA E EXIBE O BÔNUS QUE O CLIENTE DEVE PAGAR
print("Bem vindo!")

print("Abaixo estão listados os tipos de assinatura.")

print("1 - Basic")
print("2 - Silver")
print("3 - Gold")
print("4 - Platinum")

tipo_assinatura = int(input("Escolha uma das opções acima e informe o número correspondente: "))

if tipo_assinatura == 1:
    faturamento_anual = float(input("Digite o faturamento anual: "))
    valor_bonus = faturamento_anual * 0.3 # 30%
    print("O valor do bônus a ser pago é R${:.2f}".format(valor_bonus))
elif tipo_assinatura == 2:
    faturamento_anual = float(input("Digite o faturamento anual: "))
    valor_bonus = faturamento_anual * 0.2 # 20%
    print("O valor do bônus a ser pago é R${:.2f}".format(valor_bonus))
elif tipo_assinatura == 3:
    faturamento_anual = float(input("Digite o faturamento anual: "))
    valor_bonus = faturamento_anual * 0.1 # 20%
    print("O valor do bônus a ser pago é R${:.2f}".format(valor_bonus))
elif tipo_assinatura == 4:
    faturamento_anual = float(input("Digite o faturamento anual: "))
    valor_bonus = faturamento_anual * 0.05 # 20%
    print("O valor do bônus a ser pago é R${:.2f}".format(valor_bonus))
else:
    print("Opção inválida!")