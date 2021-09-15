# Sorteando uma ordem na lista
from random import shuffle
a1 = input("Quem é o primeiro aluno: ")
a2 = input("Quem é o segundo aluno: ")
a3 = input("Quem é o terceiro aluno: ")
a4 = input("Quem é o quarto aluno: ")
turma = [a4,a3,a2,a1]
shuffle(turma)   #comando "shuffle" embaralha a lista.
print("A ordem de apresentação dos trabalhos será: {}".format(turma))