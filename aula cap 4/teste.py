# utilizando modulo calc.py
import calc
# importando específicos
from calc import somar, subtrair
# importando tudo (cuidado, pode causar lentidão)
from calc import *

valorUm     = float(input("Digite um valor: "))
valorDois   = float(input("Digite outro valor: "))
soma        = somar(valorUm, valorDois)
print("Total: {}".format(soma))