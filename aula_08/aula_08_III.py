#aqui ele já traz o metodo direto para a sua pasta, por isso eu não preciso utilizar math .FUNÇÃO
from math import sqrt, ceil
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é {}'.format(num,ceil(raiz)))