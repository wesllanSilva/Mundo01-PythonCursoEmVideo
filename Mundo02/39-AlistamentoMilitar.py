#Alistamento Militar.
from datetime import date

dataHoje = date.today().year
nascimento = int(input("Digite em que ano você nasceu:"))
idade = dataHoje - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, dataHoje))
if idade == 18:
    print('Você tem que se alistar neste ano.')
elif idade < 18:
    diferenca = 18 - idade
    ano = dataHoje + diferenca
    print('Para você fazer o alistamento faltam {} anos.'.format(diferenca))
    print('Seu alistamento será em {}'.format(ano))
else:
    diferenca = idade - 18
    ano = dataHoje - diferenca
    print('Você deveria ter se alistado há {} anos.'.format(diferenca))
    print('Seu alistamento foi em {}'.format(ano))

