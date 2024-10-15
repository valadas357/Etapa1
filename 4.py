#solicita o valor do salario ao usuario
salario = float(input('Digite o salario atual:'))

#Fazendo a multiplicação dos 25% para ter o novo salario do funcionario
aumento = salario *0.25
novo_salario = salario + aumento


#Imprimimindo o valor do aumento e o valor do novo salario
print(f'O valor do aumento é: R$ {aumento:.2f}')
print(f'O novo salario com aumento de 25% é: {novo_salario:.2f}')