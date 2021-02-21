#Desenvolve um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
#até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distancia da sua viagem em Km: '))
duzentos = distancia * 0.50
maisduzentos = distancia * 0.45
if distancia <= 200:
    print('O valor a ser pago de pedagio é de R$ {:.2f}'.format(duzentos))
else:
    print('O Valor a ser pago por você é de R${:.2f}'.format(maisduzentos))
print('Boa Viagem!')