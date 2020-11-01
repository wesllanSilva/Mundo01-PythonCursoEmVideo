#CONVERSOR DE MEDIDAS
m = float(input("Digite uma distância em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(" a medida de {} metros corresponde a: \n{} kilometros \n{} hectômetros \n{} decâmetros \n{:.0f} decimetros \n{:.0f} centimetros \n{:.0f} milimetros".format(m,km,hm,dam,dm,cm,mm))

