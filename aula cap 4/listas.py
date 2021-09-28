lista = ['violão', 'guitarra', 'bateria']

# adiciona novo valor por ultimo 
lista.append(input("Digite um novo valor para adicionar a lista: "))

# adicionando novo valor em uma posição específica
lista.insert(0, input("Digite um valor para preencher a posição {}: ".format(0)))

# removendo o último valor da lista
lista.pop()

# removendo valor em posição específica
lista.pop(2)

# removendo por valor passado
lista.remove("violão")

# quantidade de vezes que o elemento aparece na lista
lista.count("violão")

# ordena a lista em ordem crescente/alfabética
lista.sort()

# inverte a ordem dos elementos da lista
lista.reverse()

# mostra a quantidade/tamanho de elementos da lista
len(lista)

# mostra a soma dos elementos
sum(lista)

# exibindo valores 
for indiceLista in lista:
    print(lista)
