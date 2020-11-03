# QUEBRANDO UM NÚMERO
from math import trunc #comando pra importar o metodo "trunc" da biblioteca "math"
n = float(input("Digite um valor: "))
 #trunc é o metodo usado pra truncar o valor para inteiro.
print("Você digitou {} e a porção inteira dele é {}".format(n,trunc(n)))