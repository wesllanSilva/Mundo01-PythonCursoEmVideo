#Aumento de salário multiplos
salario = float(input("Qual é o seu salario? R$"))
novoSalario=0
aumento = 0
if salario >= 1250:
    aumento =10
    novoSalario = salario + salario * 10/100
else:
    novoSalario = salario + salario * 15/100
    aumento = 15
print("Seu salario de R${:.2f} teve um acréscimo de {}% .\n"
      "Seu novo salário é R${:.2f}".format(salario,aumento,novoSalario))