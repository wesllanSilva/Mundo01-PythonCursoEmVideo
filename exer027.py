#PRIMEIRO E ULTIMO NOME DE UMA PESSOA
nome = str(input("DIGITE SEU NOME COMPLETO: ")).strip()
lista_nome = nome.split()
# split transforma o nome em uma lista.
nome1 = lista_nome[0].title()
#title deixa a primeira letra em maiúscula.
ultimo_nome = lista_nome[len(nome.split())-1]
#len conta quantos objetos tem na lista.
print("É um prazer te conhecer! ")
print("Seu primeiro nome é {}.".format(nome1))
print("Seu último nome é {}.".format(ultimo_nome))