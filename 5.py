#Recebendo os valores de  Salario e percentual
salario= float(input('Digite o salario atual:'))
percentual= float(input('Digite o percentual de aumento:'))

# Fazendo a soma e dividindo o percentual por 100 para ter o valor
aumento = salario+(percentual/100)
novo_salario = salario + aumento

#Imprimindo os valores para ter o valor do aumento e o novo salario
print(f'O valor do aumento é: R$ {aumento:.2f}')
print(f'O novo salario é: R$ {novo_salario:.2f}')