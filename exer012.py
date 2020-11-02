preco = float(input("Qual o preço do produto? R$ "))
novoPreco = preco - (preco * 5 /100)

print("esse produto no valor de R${} ,com desconto de 5% vai custar R${:.2f}".format(preco,novoPreco))