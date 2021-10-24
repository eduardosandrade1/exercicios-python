#apresentacao
print('*'*45,'\033[31mDesempata food\033[m','*'*45)
print('\n')

#amostra de empresas e seus dados
mineiro     = [4.2,1.7, 'O Mineiro']
amor        = [4.3,1.2, 'Amor aos pedacos']
coffee      = [4.5,.8, 'We Coffee']
kazu        = [4.6,.7, 'Lamen Kazu']
pretzels    = [4.7,1.4, 'Mr. Pretzels']
brigadeiria = [4.7,1.2, 'Brigadeiria Shop.']

#lista de restaurantes apresentada ao usuario
restaurantes = [mineiro, amor, coffee, kazu, pretzels, brigadeiria]

#estabelecido para rankeamento

troca_posicao   = []
#logica do ranking
# COMPARA UM EMPREENDIMENTO COM OS SEGUINTES
for empreendimento in range(0, len(restaurantes)):
    # O PROXIMO EMPREENDIMENTO É A POSIÇÃO ATUAL DELE NO ARRAY + 1
    for proximo_empreendimento in range( (empreendimento + 1), len(restaurantes)):

        nota_empreendimento         = restaurantes[empreendimento][0]
        nota_proximo_empreendimento = restaurantes[proximo_empreendimento][0]

        if nota_empreendimento < nota_proximo_empreendimento:
            troca_posicao                       = restaurantes[proximo_empreendimento]
            restaurantes[proximo_empreendimento]    = restaurantes[empreendimento]
            restaurantes[empreendimento]            = troca_posicao
            
        elif nota_empreendimento > nota_proximo_empreendimento:
            troca_posicao               = restaurantes[empreendimento]
            restaurantes[empreendimento]    = restaurantes[proximo_empreendimento]
            restaurantes[empreendimento]    = troca_posicao

            # se tiver nota igual, avalia a distância            
        elif nota_empreendimento == nota_proximo_empreendimento:

            distancia_empreendimento            = restaurantes[empreendimento][1]
            distancia_proximo_empreendimento    = restaurantes[proximo_empreendimento][1]

            # se a distancia do empreendimento for menor do que a do PROXIMO empreendimento
            if distancia_empreendimento > distancia_proximo_empreendimento:
                troca_posicao                       = restaurantes[proximo_empreendimento]
                restaurantes[proximo_empreendimento]    = restaurantes[empreendimento]
                restaurantes[empreendimento]            = troca_posicao
            else:
                troca_posicao               = restaurantes[empreendimento]
                restaurantes[empreendimento]    = restaurantes[proximo_empreendimento]
                restaurantes[empreendimento]    = troca_posicao

# exibicao ordenada das melhores opcoes
print('A seguir o ranking das melhores opcoes baseadas nos criterios de nota e distancia da sua casa:\n')
for item in restaurantes:
    print("{} --- Km: {} --- {} ".format(item[0], item[1], item[2]))