#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual é o preço do produto:'))
porcento = produto - (produto * 5 / 100)
print("O produto que custava R${}, na promoção com desconte de %5 vai custar R${:.2f}".format(produto,porcento))
