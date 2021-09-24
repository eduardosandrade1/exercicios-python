# RECEBE:
# valor numérico inteiro e verificar se o número existe na sequência de Fibonacci
# 1,1,2,3,5,8,13,21,34... sempre a soma dos dois números anteriores
print("!---------- DESCOBRINDO A NÚMERO DE FIBONACCI ----------!")

numero      = int(input("Informe um número: "))
ultimo      = 1
penultimo   = 1
soma        = 1
# Se a soma dos dois últimos números for menor que o número solicitado,
# será comparado o último valor atribuído com o valor solicitado para ver se pertence a sequência
while soma < numero:
    # somando os primeiros numeros
    soma       = ultimo + penultimo
    # fazendo o penultimo numero ser o ultimo valor
    penultimo   = ultimo
    # e o ultimo valor ser o total da soma
    ultimo      = soma

if ultimo == numero:
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")