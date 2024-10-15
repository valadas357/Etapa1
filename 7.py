#solicitando o numero da temperatura para fazer a transformação
fahrenheit = float(input('Digite a temperatura em fahrenheit:'))

#convertendo o valor em fahrenehit para celcius
celcius = 5/9* (fahrenheit - 32)

#Imprimindo o valor transformado de fahrenheit para celcius
print(f'A temperatura em trasnformada de fahrenheit para celcius é: {celcius:.2f}')