# recebe: Batimento Por Minuto e a idade
batimento = int(input("Informe o BPM(Batimento Por Minuto): "))
idade = int(input("Informe sua idade: "))

if idade <= 2 and batimento > 140:
    print("Batimentos está ACIMA da faixa adequada. ")
elif idade <= 2 and batimento < 120:
    print("Batimentos está ABAIXO da faixa adequada. ")
elif idade <= 17 and batimento > 100:
    print("Batimentos está ACIMA da faixa adequada. ")
elif idade <= 17 and batimento < 80:
    print("Batimentos está ABAIXO da faixa adequada. ")
elif idade <= 65 and batimento > 80:
    print("Batimentos está ACIMA da faixa adequada. ")
elif idade <= 65 and batimento < 70:
    print("Batimentos está ABAIXO da faixa adequada. ")
else:
    print("Batimentos está DENTRO da faixa adequada. ")