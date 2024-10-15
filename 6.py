# solicitando o valor da base
salario_base = float(input('Digite o salario base:'))

#Calculando todos os valores somando e no final diminuindo pelo imposto
gratificaçao = 50.0
imposto = salario_base * 0.10
salario_a_receber = salario_base + gratificaçao - imposto

#Imprimindo os valores a pagar do imposto e o salario a receber do funcionario
print(f'O valor do imposto a ser pago é: R$ {imposto:.2f}')
print(f'O valor do salaro a receber é: R$ {salario_a_receber:.2f}')
