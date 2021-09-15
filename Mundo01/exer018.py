# SENO, COSENO E TANGENTE.
import math
ang = float(input("Digite o valor do Ângulo: "))
# É convertido o valor de "ang" que esta em graus para valor radiano
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
ta = math.tan(math.radians(ang))
print("Com o ângulo de {} \n"
      "O seno é {:.2f}, \n"
      "O coseno é {:.2f} \n"
      "A tangente é {:.2f}".format(ang,se,co,ta))