#REAJUSTE SALÁRIAL
salario = float(input("Qual é o salário do funcionário? R$ "))
novoSalario = salario + (salario * 15 /100)

print("O funcionário que recebia R${} ,com o aumento 15% vai ter o novo salário de R${:.2f}".format(salario,novoSalario))