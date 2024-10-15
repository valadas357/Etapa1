#Importa a biblioteca math para calculos
import math

#Solicita ao usuario um numero positivo maior que 0
numero = float(input('Digite um numero positivo maior que 0: '))

#Faz as operações em cada opção
if numero > 0:
    quadrado = numero * numero
    cubo = numero *numero * numero
    raiz_quadrada = math.sqrt(numero)
    raiz_cubica = numero ** (1/3)
    
#Imprime os valores corretor de cada numero
print(f'O numero digitado ao quadrado é: {quadrado:.2f}')
print(f'O numero digitado ao cubo é: {cubo:.2f}')
print(f'O numero digitado em raiz quadrada é:{ raiz_quadrada:.2f}')
print(f'O numero digitado em raiz cubica é: {raiz_cubica:.2f}')