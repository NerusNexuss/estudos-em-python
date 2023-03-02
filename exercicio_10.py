#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input("Quantos dinherio você tem na carteira ? R$" ))
valor_dolar = carteira/5.21
print("com {} você pode comprar US${:.3}".format(carteira,valor_dolar))

