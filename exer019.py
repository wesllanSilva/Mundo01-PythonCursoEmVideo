# Sorteando um item na lista
from random import choice
# "randon" pega um um nùmero ou strin aleatório.
a1 = input("Quem é o primeiro aluno: ")
a2 = input("Quem é o segundo aluno: ")
a3 = input("Quem é o terceiro aluno: ")
a4 = input("Quem é o quarto aluno: ")
sala = [a1,a2,a3,a4]
aluno = choice(sala)
print("o aluno sorteado foi {}".format(aluno.upper())) # o ".upper" coloca em maiúculo.