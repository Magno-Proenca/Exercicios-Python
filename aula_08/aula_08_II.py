# se usarmos mat.ceil() arredondamos para cima o valor da raiz
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}.' .format(num, math.ceil(raiz)))
