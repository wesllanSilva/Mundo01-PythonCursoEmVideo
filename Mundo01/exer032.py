#ANO BISSEXTO.
from datetime import date
ano = int(input("Digite qual ano você quer analisar: "))
if ano == 0:
    ano = date.today().year
    #importada a biblioteca de data para pegar o ano atual da máquina do usuário.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é um ano BISSEXTO!".format(ano))
else:
    print("O ano de {} Não é BISSEXTO!".format(ano))