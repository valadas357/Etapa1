# Escreva um algoritmo que leia os valores dos catetos de um triângulo retângulo e mostre
#qual é o valor da hipotenusa desse triângulo.
cateto1 = float(input('Digite o numero do primeiro cateto: '))
cateto2 = float(input('Digite o numero do segundo cateto: '))

hipotenusa = (cateto1 / cateto2)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

