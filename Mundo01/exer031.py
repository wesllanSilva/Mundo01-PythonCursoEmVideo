#CUSTO DA VIAGEM
km = float(input("Qual a distância da viagem em KM? "))
if km <= 200:
    valor = km * 0.50
    print("A viagem de {}km, fica no valor de R${:.2f}".format(km,valor))
else:
    valor = km * 0.45
    print("A viagem de {}km, fica no valor de R${:.2f}".format(km,valor))