# RECEBE: QUANTIDADE DE VOTOS POR CADA DIA DA SEMANA
# MOSTRA QUAL DIA FOI ESCOLHIDO (MAIOR VALOR)

print("Bem vindo!")
sunday_vote = int(input("Digite a quantidade de votos para o DOMINGO: "))
monday_vote = int(input("Digite a quantidade de votos para o SEGUNDA-FEIRA: "))
tuesday_vote = int(input("Digite a quantidade de votos para o TERÇA-FEIRA: "))
wednesday_vote = int(input("Digite a quantidade de votos para o QUARTA-FEIRA: "))
thursday_vote = int(input("Digite a quantidade de votos para o QUINTA-FEIRA: "))
friday_vote = int(input("Digite a quantidade de votos para o SEXTA-FEIRA: "))
sabbat_vote = int(input("Digite a quantidade de votos para o SÁBADO: "))

if sunday_vote > monday_vote and sunday_vote > tuesday_vote and sunday_vote > wednesday_vote and sunday_vote > thursday_vote and sunday_vote > friday_vote and sunday_vote > sabbat_vote:
    print("DOMINGO foi o dia escolhido.")
elif monday_vote > tuesday_vote and monday_vote > wednesday_vote and monday_vote > thursday_vote and monday_vote > friday_vote and monday_vote > sabbat_vote and monday_vote > sunday_vote:
    print("SEGUNDA-FEIRA foi o dia escolhido.")
elif tuesday_vote > wednesday_vote and tuesday_vote > thursday_vote and tuesday_vote > friday_vote and tuesday_vote > sabbat_vote and tuesday_vote > sunday_vote and tuesday_vote > monday_vote:
    print("TERÇA-FEIRA foi o dia escolhido.")
elif wednesday_vote > thursday_vote  and wednesday_vote > friday_vote and wednesday_vote > sabbat_vote and wednesday_vote > sunday_vote and wednesday_vote > monday_vote and wednesday_vote > tuesday_vote:
    print("QUARTA-FEIRA foi o dia escolhido.")
elif thursday_vote > friday_vote and thursday_vote > sabbat_vote and thursday_vote > sunday_vote and thursday_vote > monday_vote and thursday_vote > tuesday_vote and thursday_vote > wednesday_vote:
    print("QUINTA-FEIRA foi o dia escolhido.")
elif friday_vote > sabbat_vote and friday_vote > sunday_vote and friday_vote > monday_vote and friday_vote > tuesday_vote and friday_vote > wednesday_vote and friday_vote > thursday_vote:
    print("SEXTA-FEIRA foi o dia escolhido.")
elif sabbat_vote > sunday_vote and sabbat_vote > monday_vote  and sabbat_vote > tuesday_vote and sabbat_vote > wednesday_vote and sabbat_vote > thursday_vote and sabbat_vote > friday_vote:
    print("SÁBADO foi o dia escolhido.")
else:
    print("Nenhum dia foi escolhido, faça a votação novamente!")