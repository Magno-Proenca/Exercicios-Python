#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade que você estava em Km/h: '))
if velocidade > 80:
    pagar = ((velocidade - 80) * 7)
    print('Você deverá pagar a multa de R${:.2f} '.format(pagar))
else:
    print('Parabéns você está dentro limite de velocidade permitido')
