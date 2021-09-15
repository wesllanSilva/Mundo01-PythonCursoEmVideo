#PINTURA DE PAREDE.
largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
litros = area/2
print("Sua parede tem dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede você vai precisar de {}l de tinta.".format(largura,altura,area,litros))