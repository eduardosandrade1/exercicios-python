# Exercício feito na primeira aula da FIAP
# este programa recebe a distancia e o tempo
print("Esse é o calculador de velocidade média")

distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")

velocidade_media = float(distancia) / float(tempo)

print("A velocidade media é de {:.2f} m/min".format(velocidade_media))