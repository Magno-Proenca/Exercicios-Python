#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
num = float(input('Digite um numero para ter sua parcela inteira: '))
inteiro = math.floor(num)
print('A parte inteira de {} é {}'.format(num, inteiro))