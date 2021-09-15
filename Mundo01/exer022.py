# MANIPULANDO TEXTO.
nome = input("digite seu nome completo: ").strip()
# O .strip ja corta os espaços do começo e do final se o usuário adicionar
maiusc = nome.upper()
minusc =  nome.lower()
tot_nome = len(nome) - nome.count(" ")
# O count() conta conta quantos espaços que foram digitados.
# subtrai o total de caracteres pelo quantidade de espaços.
li_nome = nome.split()
#O split() separa a string colocando as palavras em lista
print("Seu nome em maiúsculo é: {}\n"
      "Seu nome em minúsculo é : {}\n"
      "Seu nome tem {} letras.".format(maiusc,minusc,tot_nome))
print("Seu primeiro nome é: {} e ele tem {} letras".format(li_nome[0],len(li_nome[0])))

