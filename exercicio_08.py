#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

numero = float(input("Digite um valor em metros:"))

print("A medida de {}m corresponde a {}cm {}nm".format(numero,(numero*100),(numero*1000)))
