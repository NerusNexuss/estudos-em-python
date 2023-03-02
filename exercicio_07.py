#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
media = (nota1+nota2)/2

print("A media entre a nota {:.1f} é nota {:.1f} é igual a {:.1f}.".format(nota1,nota2,media))