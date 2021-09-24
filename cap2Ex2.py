# recebe VALOR BRUTO do pacote, categoria dos assentos no vôo e qtd de viajantes
print("Bem vindo!")
valorBrutoViagem = float(input("Por favor, nos informe o VALOR BRUTO do pacote da viagem: "))
print(" ")
print("Agora, nos informe o número correspondente a categoria do vôo. ")
print("1 - Econômica. ")
print("2 - Executiva. ")
print("3 - Primeira classe. ")

categoria = int(input("Informe o número da categoria: "))
qtdViajantes = int(input("Informe a quantidade de viajantes: "))

if categoria == 1:

    print("Valor Bruto: R${:.2f}. ".format(valorBrutoViagem))
    if qtdViajantes == 2:
        desconto = valorBrutoViagem * 0.03
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes == 3:
        desconto = valorBrutoViagem * 0.04
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes > 4:
        desconto = valorBrutoViagem * 0.05
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    else:
        print("Por favor, digite mais de um passageiro!")
elif categoria == 2:

    if qtdViajantes == 2:
        desconto = valorBrutoViagem * 0.05
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes == 3:
        desconto = valorBrutoViagem * 0.07
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes > 4:
        desconto = valorBrutoViagem * 0.08
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    else:
        print("Por favor, digite mais de um passageiro!")
elif categoria == 3:

    if qtdViajantes == 2:
        desconto = valorBrutoViagem * 0.1
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes == 3:
        desconto = valorBrutoViagem * 0.15
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    elif qtdViajantes > 4:
        desconto = valorBrutoViagem * 0.20
        mediaPorViajante = float(valorBrutoViagem / qtdViajantes)
        print("Valor de desconto é de R${:.2f}.".format(desconto))
        print("Valor LÍQUIDO é de R${:.2f}".format(valorBrutoViagem - desconto))
        print("A média por viajante é de R${:.2f}".format(mediaPorViajante))
    else:
        print("Por favor, digite mais de um passageiro!")
else:
    print("Categoria inexistente!")