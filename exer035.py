# ANALISANDO UM TRIÂNGULO v1.0
r1 = float(input("Qual o cumprimento da reta 1 ?"))
r2 = float(input("Qual o cumprimento da reta 2 ?"))
r3 = float(input("Qual o cumprimento da reta 3 ?"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("As retas podem formar um triângulo")
else:
    print("As retas não podem formar um triângulo")
