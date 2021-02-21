#faça um programa que leia o comprimento do cateto oposto e do cateto adjascente
#de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = ((co**2) + (ca**2))**(1/2)
print('A hipotenusa é {}.'.format(hip))

