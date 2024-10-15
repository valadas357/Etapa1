# Solicita uma palavra para o usuario
palavra = input('Digite uma palavra: ')

#Faz o calculo da quantidade de letras
quantidade_letras = len(palavra)


#Faz a verificação da quantidade de letras se e par ou impar
if quantidade_letras % 2 == 0:

   #Imprime se as palavra tem letras impares ou pares
    print('A quantidade de letras é par.')
else: print('A quantidade de letras e impar.')