#condições simplificadas
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/ 2
print('Sua média foi de {:.1f}'.format(media))
print('Parabéns!!!' if 5 <= media else 'Você precisa estudar mais')#condição simplificada