#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
ang = input('Digite o valor do angulo: ')
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = float(input('Digite a hipotenusa: '))
sen = co/hip
cos = ca/hip
tg = co/ca
print('O seno, cosseno e tangente do angulo de {} '.format(ang), end='')
#lembrando que o end='' le-se , ao final da linha não vai ter nada, logo nao ha a quebra da linha
print('são respectivamente {:.3f},{:.3f} e {:.3f}.'. format(sen, cos, tg))
