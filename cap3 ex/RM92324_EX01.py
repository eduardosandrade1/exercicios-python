# recebe:
# Quantidade de alimentos consumidos no dia
# numero de caloriasde cada um dos alimentos

print("!---------- HEALTH TRACK - ALIMENTOS CONSUMIDOS ----------!")

quantidade_de_alimentos = int(input("Por favor, digite a quantidade de alimentos consumidos hoje: "))
#inicializando variavel de calorias para ela poder somar com ela mesma
total_de_calorias = 0
# para quantidade de alimentos informada pelo usuário
for i in range(0, quantidade_de_alimentos):
    quantidade_de_calorias = float(input("Digite a quantidade de calorias do {}° alimento: ".format(i+1)))
    total_de_calorias += quantidade_de_calorias
# exibindo total de calorias
print("Você consumiu {} kcal hoje! ".format(total_de_calorias))