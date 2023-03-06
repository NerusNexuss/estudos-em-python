#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o valor do funcionário!R$'))
aumento = salario + (salario * 15 / 100)
print("um funcionario que ganhava R${}, com 15% de aumento, passa a receber R${}".format(salario,aumento))


