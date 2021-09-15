#Aprovando Emprestimo!
valor_casa = float(input("Valor da casa: R$"))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: R$'))
parcela = valor_casa / (anos * 12)
dinheiro = salario * 30/100

print('Para pagar uma casa de R${:.2f}  em {} anos a parcela vai ter o valor de R${:.2f}.'.format(valor_casa,anos,parcela))
if parcela > dinheiro:
    print('Empréstimo NEGADO!')
else:
    print('Emprestimo APROVADO!')