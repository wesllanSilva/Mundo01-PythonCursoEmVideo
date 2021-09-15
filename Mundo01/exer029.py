#RADAR ELETRÔNICO
v = float(input("qual a velocidade do carro? "))
if v <=80:
    print("Você esta dirigindo dentro do limite permitido.")
else:
    v2 = (v - 80)* 7
    print("ACIMA DO LIMITE DE 80 KM/H. Vocẽ será MULTADO em R${} ".format(v2))