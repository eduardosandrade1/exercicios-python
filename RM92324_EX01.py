# RECEBE: PESO E ALTURA
# CALCULA  IMC (PESO / ALTURA²)
print("!------ CALCULADORA DE IMC ------!")
print(" ")
peso = float(input("Por favor, digite seu peso atual: "))
altura = float(input("Por favor, digite sua altura: "))

# altura ao quadrado
altura = altura * altura

imc = peso / altura

if imc < 16.00:
    print("Baixo peso Grau III")
elif imc < 16.99:
    print("Baixo peso Grau II")
elif imc < 18.49:
    print("Baixo peso Grau I")
elif imc < 24.99:
    print("Peso ideal")
elif imc < 29.99:
    print("Sobrepeso")
elif imc < 34.99:
    print("Obesidade Grau I")
elif imc < 39.99:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")