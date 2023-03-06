#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em C:"))
f = (celsius * 1.8) + 32


print("A temperatura de {} corresponde a {}F".format(celsius,f))