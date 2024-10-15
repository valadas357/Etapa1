num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segudo numero: "))
num3 = float(input("Digite o terceiro numero: "))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 >= num2:
    maior = num3

menor = num1
if num2 < num3 and num2 < num1:
    menor = num2

if num3 <= num2 and num3 < num1:
    menor = num3

print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')