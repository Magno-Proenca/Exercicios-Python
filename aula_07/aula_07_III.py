n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
p = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma destes dois numeros é {}, o produto é {} e a divisão é {:.3f}, '.format(s, p, d), end='')
#O end='' le-se , ao final da linha não vai ter nada, logo nao ha a quebra da linha
print('a divisão inteira é {} e a exponenciação é {}'.format(di, e))