'''
Faça um algoritmo que simule uma calculadora simples. O usuário deve escolher (uma)
operação básica: adição, subtração, multiplicação, divisão e potenciação. Feito isso, o
usuário deve entrar com dois números quaisquer e o programa deve realizar a operação
mostrando o resultado correto.

'''
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input("Digite o segundo numero: "))


print('-'*25)


print("Opção adição digite: +")
print("Opção subtração digite: -")
print("Opção multiplicação digite: *")
print("Opção divisão digite: /")
print("Opção potenciação digite: **")

adicao = num1 + num2

sub = num1 - num2

mult = num1 * num2

div = num1 / num2


pot = num1 ** num2

operacao = input('Escolha a operacao: ')
if operacao == '+':
    print(f"A soma é = {adicao}")

elif operacao == '-':
    print(f'A subtração é = {sub}')

elif operacao == '*':
    print(f'A multiplicação é = {mult}')

elif operacao == '/':
    print(f'A divisão é = {div}')

elif operacao == '**':
    print(f'A potenciação é = {pot}')

else:
    print("Operação inválida! ")

