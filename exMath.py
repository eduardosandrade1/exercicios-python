import math

a = float(input("Digite o valor de A"))
b = float(input("Digite o valor de B"))
c = float(input("Digite o valor de C"))

delta = b * b - 4 * a * c

if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a,b,c,x1,x2))
elif delta == 0:
    #cálculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a,b,c,x))
else:
    #exibição da mensagem
    print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))