n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
p = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma destes dois numeros é {},\n o produto é {} e a divisão é {:.3f}, '.format(s, p, d), end='')
#o \n serve para quebrar a linha
print('a divisão inteira é {} \n e a exponenciação é {}'.format(di, e))