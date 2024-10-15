#Solicitando 4 numeros da placa do usuario
placa = input('Digite os 4 números da placa do automavel:')

#Fazendo a comparação do numero da placa com o mes
if len(placa) ==4 and placa.isdigit():

    ultimo_digito = int(placa[-1])

if ultimo_digito ==0:
    mes_vencimento = 'Janeiro'
elif ultimo_digito ==1:
    mes_vencimento = 'Fevereiro'
elif ultimo_digito ==2:
    mes_vencimento = 'Março'
elif ultimo_digito ==3:
    mes_vencimento = 'Abril'
elif ultimo_digito ==4:
    mes_vencimento = 'Maio'
elif ultimo_digito ==5:
    mes_vencimento = 'Junho'
elif ultimo_digito ==6:
    mes_vencimento = 'Julho'
elif ultimo_digito ==7:
    mes_vencimento = 'Agosto'
elif ultimo_digito ==8:
    mes_vencimento = 'Setembro'
elif ultimo_digito ==9:
    mes_vencimento = 'Outubro'

    #Imprimindo o mes do vencimento 
    print(f'O mes de vencimento do IPVA è: {mes_vencimento}')
    print(f'Por favor, Digite apenas 4 numeros da placa.')