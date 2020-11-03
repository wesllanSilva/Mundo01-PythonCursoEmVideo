# Catetos e Hipotenusa
from math import hypot
# metodo "hypot" calcula a hipotenusa
oposto = float(input("Qual o cumprimento do cateto oposto? "))
adjacente = float(input("Qual o cumprimento do cateto adjacente? "))
print("Com o oposto no valor de {} e o adjacente {} \na hipotenusa vale {:.2f}".format(oposto,adjacente,hypot(oposto,adjacente)))