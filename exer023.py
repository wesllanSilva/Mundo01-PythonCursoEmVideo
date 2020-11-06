# Separando digitos de um número
num = int(input("Digite um número de 0 até 9999: "))
# É feita a divisão inteira do número e depois o resta da divisão.
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print("A unidade do número digitado é {}.\n"
      "A dezena dele é {}.\n"
      "A centena dele é {}.\n"
      "O milhar dele é {}.".format(uni,dez,cen,mil))