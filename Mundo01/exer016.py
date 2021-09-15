# QUEBRANDO UM NÚMERO
import math #comando pra importar biblioteca "math"
n = float(input("Digite um valor: "))
r = math.trunc(n) #trunc é o metodo usado pra truncar o valor para inteiro.
print("Você digitou {} e a porção inteira dele é {}".format(n,r))