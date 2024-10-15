#Solicita ao usuario um numero entre 1 e 7
numero = int(input('Digite um numero inteiro entre o 1 e 7: '))


#Imprime o numero do dia da semana junto com o dia escrito
if numero == 1:
    print('Domingo')
elif numero ==2:
    print('Segunda feira')
elif numero ==3:
    print('Terça feira')
elif numero ==4:
    print('Quarta feira')
elif numero ==5:
    print('Quinta feira')
elif numero ==6:
    print('Sexta feira')
elif numero ==7:
    print('Sabado')
else:
    print('Não existe dia de semana com esse numero. ')