#ALUGUEL DE CARRO.
km = float(input("Quantos kilometros o carro percorreu? "))
dias = float(input("Por quantos dias o carro ficou alugado? "))
valor = (km * 0.15) + (dias * 60)
print("O valor total a ser pago é de R${}".format(valor))