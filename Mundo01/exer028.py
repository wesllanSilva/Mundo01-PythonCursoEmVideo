#JOGO DA ADIVINHAÇÃO V1.0
from random import randint
#importei a biblioteca random pra sortear um número.
n = randint(0,5)
n1 = int(input("Estou pensando em um número entre 0 e 5.\nQual número eu pensei? "))
print("EU escolhi o número {}. \nE você escolheu o número {}: ".format(n,n1))
if n == n1:
    print("Você acertou, PARABÉNS!")
else:
    print("Você errou!")