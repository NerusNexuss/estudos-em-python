#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

parede = float(input("Largura da parede:"))
altura_parede = float(input('Altura da parede:'))
area = parede*altura_parede
pintar = area/2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m2".format(parede,altura_parede,area))
print("Para pintar essa parede, você precisará de{}l de tinta".format(pintar))
