#Exemplo 2

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/ 2
if media >= 5:
    print('Muito bem, sua media é de {:.1f} e está ótima!'.format(media))#{:.1f}formatação para uma casa decimal
else:
    print('Sua média é de {:.1f}, você precisa estudar mais!'.format(media))
print('Boa sorte nos estudos!')
